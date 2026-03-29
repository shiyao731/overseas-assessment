#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数据质量校验脚本 v2.1.0
用于验证搜集到的企业出海数据的质量和完整性
支持分层评分、替代指标、多地域合规评估
"""

import json
from datetime import datetime
from typing import Dict, List, Any, Optional

class DataValidator:
    """数据质量校验器 v2.1.0"""

    def __init__(self):
        self.errors = []
        self.warnings = []
        self.info = []
        self.score = 100

    def determine_development_stage(self, data: Dict[str, Any]) -> str:
        """
        判定企业发展阶段

        返回: '初创期' | '成长期' | '成熟期' | '未知'
        """
        # 检查是否上市
        is_listed = data.get('is_listed', False)

        # 检查成立时间
        founded_year = data.get('founded_year')
        years_since_founded = None
        if founded_year:
            years_since_founded = datetime.now().year - founded_year

        # 检查营收
        revenue = data.get('revenue')
        if isinstance(revenue, str):
            try:
                revenue = float(revenue.replace('亿', '').replace('万', ''))
            except:
                pass

        # 检查团队规模
        team_size = data.get('team_size')

        # 判定逻辑
        if is_listed or (revenue and revenue >= 10) or (years_since_founded and years_since_founded > 7):
            return '成熟期'
        elif (years_since_founded and years_since_founded >= 3) or \
             (team_size and team_size >= 50) or \
             data.get('funding_round') in ['B轮', 'C轮', 'D轮']:
            return '成长期'
        elif (years_since_founded and years_since_founded < 3) or \
             (team_size and team_size < 50) or \
             data.get('funding_round') in ['种子轮', '天使轮', 'A轮']:
            return '初创期'
        else:
            return '未知'

    def validate_company_basic_info(self, data: Dict[str, Any]) -> bool:
        """验证企业基本信息"""
        required_fields = ['company_name', 'main_business']
        missing = [f for f in required_fields if not data.get(f)]

        if missing:
            self.errors.append(f"企业基本信息缺失字段: {', '.join(missing)}")
            self.score -= 20
            return False

        # 判定发展阶段
        stage = self.determine_development_stage(data)
        data['development_stage'] = stage
        self.info.append(f"企业发展阶段判定: {stage}")

        return True

    def validate_financial_data(self, data: Dict[str, Any]) -> bool:
        """验证财务数据（支持替代指标）"""
        stage = data.get('development_stage', '未知')

        # 检查是否有财务数据
        has_revenue = data.get('revenue') is not None
        has_funding = data.get('funding_round') is not None or data.get('funding_amount') is not None
        has_valuation = data.get('valuation') is not None

        if stage == '成熟期':
            # 成熟期企业必须有财务数据
            if not has_revenue:
                self.warnings.append("成熟期企业缺少营收数据，建议补充年报或招股书")
                self.score -= 10
            else:
                # 检查数据时效性
                year = data.get('fiscal_year')
                if year and year < 2024:
                    self.warnings.append(f"财务数据较旧（{year}年），建议使用最新数据")
                    self.score -= 5
        else:
            # 初创/成长期企业可以使用替代指标
            if not has_revenue and not has_funding and not has_valuation:
                self.warnings.append("缺少财务数据或替代指标（融资/估值），建议补充至少一项")
                self.score -= 5
            elif has_funding or has_valuation:
                self.info.append("使用替代指标（融资/估值）进行财务评估")

        return True

    def validate_patent_data(self, data: Dict[str, Any]) -> bool:
        """验证专利/技术数据（支持替代指标）"""
        stage = data.get('development_stage', '未知')
        industry = data.get('industry', '')

        has_patents = data.get('patents') is not None
        has_rd_investment = data.get('rd_investment') is not None
        has_funding = data.get('funding_round') is not None
        has_team_background = data.get('team_background') is not None
        has_growth_rate = data.get('user_growth_rate') is not None

        if stage == '成熟期':
            # 成熟期企业优先使用专利数据
            if not has_patents and not has_rd_investment:
                self.warnings.append("缺少专利或研发投入数据，技术维度评分可能不准确")
                self.score -= 5
        else:
            # 初创/成长期企业可以使用替代指标
            if not any([has_patents, has_rd_investment, has_funding, has_team_background, has_growth_rate]):
                self.warnings.append("缺少技术数据或替代指标（融资/团队/增长率），建议补充至少一项")
                self.score -= 5
            elif not has_patents:
                self.info.append("使用替代指标（融资/团队/增长率）进行技术评估")

        return True

    def validate_source_citation(self, data: Dict[str, Any]) -> bool:
        """验证数据来源标注（支持替代指标标注）"""
        sources = data.get('sources', [])
        if not sources or len(sources) == 0:
            self.errors.append("缺少数据来源标注")
            self.score -= 15
            return False

        # 检查是否标注了数据类型
        data_types = data.get('data_types', [])
        if not data_types or len(data_types) == 0:
            self.warnings.append("未标注数据类型（官方数据/替代指标/行业推演），建议补充")
            self.score -= 3

        # 检查来源可靠性
        reliable_sources = ['年报', '招股书', '官网', '国家知识产权局']
        has_reliable = any(s in str(sources) for s in reliable_sources)

        if has_reliable:
            self.info.append("包含官方数据源，数据可靠性高")
        else:
            self.warnings.append("缺少官方数据源，主要依赖替代指标或第三方数据")
            self.score -= 5

        return True

    def validate_overseas_data(self, data: Dict[str, Any]) -> bool:
        """验证海外数据（初创期企业放宽要求）"""
        stage = data.get('development_stage', '未知')

        overseas_subsidiaries = data.get('overseas_subsidiaries')
        overseas_team = data.get('overseas_team')
        overseas_users = data.get('overseas_users_percentage')

        has_any_overseas_data = any([overseas_subsidiaries, overseas_team, overseas_users])

        if stage == '成熟期':
            if not has_any_overseas_data:
                self.warnings.append("成熟期企业缺少海外布局数据，国际化维度评分可能偏高")
        else:
            # 初创/成长期企业没有海外布局是正常的
            if not has_any_overseas_data:
                self.info.append("初创/成长期企业暂无海外布局数据（正常情况）")

        return True

    def validate_target_market(self, data: Dict[str, Any]) -> bool:
        """验证目标市场数据"""
        target_market = data.get('target_market')
        if not target_market:
            self.warnings.append("未明确目标市场区域（欧美/亚太/中东/拉美/非洲），合规评估可能不准确")
            self.score -= 5
        else:
            self.info.append(f"目标市场区域: {target_market}")

        return True

    def get_validation_report(self) -> str:
        """生成校验报告"""
        report = []
        report.append("# 📊 数据质量校验报告 v2.1.0\n")

        # 总体评分
        grade = "优秀" if self.score >= 90 else "良好" if self.score >= 70 else "一般" if self.score >= 50 else "差"
        report.append(f"## 总体评分: {self.score}/100 ({grade})\n")

        # 信息提示
        if self.info:
            report.append("## 📋 信息提示")
            for info in self.info:
                report.append(f"- {info}")
            report.append("")

        # 错误
        if self.errors:
            report.append("## ❌ 错误 (必须修复)")
            for error in self.errors:
                report.append(f"- {error}")
            report.append("")

        # 警告
        if self.warnings:
            report.append("## ⚠️ 警告 (建议处理)")
            for warning in self.warnings:
                report.append(f"- {warning}")
            report.append("")

        # 建议
        if self.score < 80:
            report.append("## 💡 改进建议")
            if self.score < 50:
                report.append("- 数据质量较差，建议重新搜集核心数据")
            else:
                report.append("- 数据质量一般，建议补充官方数据源")
                report.append("- 对于非上市企业，可以使用融资、团队背景等替代指标")

        return "\n".join(report)


def validate_assessment_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    校验评估数据的主函数 v2.1.0

    参数:
        data: 包含企业出海相关数据的字典

    返回:
        包含校验结果的字典
    """
    validator = DataValidator()

    # 执行各项校验
    validator.validate_company_basic_info(data)
    validator.validate_financial_data(data)
    validator.validate_patent_data(data)
    validator.validate_source_citation(data)
    validator.validate_overseas_data(data)
    validator.validate_target_market(data)

    # 生成报告
    report = validator.get_validation_report()

    return {
        'score': validator.score,
        'errors': validator.errors,
        'warnings': validator.warnings,
        'info': validator.info,
        'report': report,
        'development_stage': data.get('development_stage', '未知'),
        'grade': "优秀" if validator.score >= 90 else "良好" if validator.score >= 70 else "一般" if validator.score >= 50 else "差"
    }


if __name__ == "__main__":
    # 示例1：成熟期企业
    mature_company = {
        'company_name': '示例制造企业',
        'main_business': '新能源车制造',
        'revenue': '5000亿',
        'fiscal_year': 2025,
        'is_listed': True,
        'founded_year': 2010,
        'patents': {'invention': 150},
        'sources': ['年报', '官网'],
        'overseas_subsidiaries': ['美国', '欧洲'],
        'target_market': '欧美'
    }

    # 示例2：初创期企业
    startup_company = {
        'company_name': '示例SaaS初创企业',
        'main_business': '企业协作软件',
        'funding_round': 'B轮',
        'funding_amount': '2亿',
        'valuation': '10亿',
        'founded_year': 2023,
        'team_size': 30,
        'user_growth_rate': '120%',
        'team_background': '创始人来自BAT',
        'sources': ['36氪', '创始人访谈'],
        'data_types': ['替代指标', '替代指标', '替代指标'],
        'target_market': '东南亚'
    }

    print("=== 示例1：成熟期企业 ===")
    result1 = validate_assessment_data(mature_company)
    print(result1['report'])
    print(f"\n最终评分: {result1['score']}/100 ({result1['grade']})")
    print(f"发展阶段: {result1['development_stage']}")

    print("\n\n=== 示例2：初创期企业 ===")
    result2 = validate_assessment_data(startup_company)
    print(result2['report'])
    print(f"\n最终评分: {result2['score']}/100 ({result2['grade']})")
    print(f"发展阶段: {result2['development_stage']}")
