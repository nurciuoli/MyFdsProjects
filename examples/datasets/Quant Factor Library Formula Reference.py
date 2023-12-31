# #Identified formulas for the factor analysis

# formulas = {
  
#  'Target_Price_Returns_1M': "P_PRICE_RETURNS(0,-1/0/0,0)",
#  'Target_Price_Returns_1M_Quintile': "UQUINTILE(#L.L1 ,P_PRICE_RETURNS(0,0,-1/0/0))",
#  'Sector':'FG_GICS_SECTOR',
#  'CTRY_CONC': 'QFL_CTRY_CONC(0)',
#  'MV': 'QFL_MKT_VAL(0)',
#  'EV': 'QFL_EV',
#  'MIDCAP': 'QFL_MIDCAP(0)',
#  'NUM_EMP': 'QFL_NUM_EMP(0)',
#  'SALES': 'QFL_SALES(0)',
#  'ASSETS': 'QFL_ASSETS(0)',
#  'BOOK': 'QFL_BV(0)',
#  'MKT_SHR_ECON': 'QFL_MKT_SHR(0,ECON,CT)',
#  'MKT_SHR_SECT': 'QFL_MKT_SHR(0,SECT,CT)',
#  'MKT_SHR_SUBSECT': 'QFL_MKT_SHR(0,SUBSECT,CT)',
#  'MKT_SHR_INDGRP': 'QFL_MKT_SHR(0,INDGRP,CT)',
#  'Value - DIV_YLD': 'AVG(QFL_DY(0,CT),QFL_DY(0,FY1),QFL_DY(0,FY2))',
#  'Value - EY': 'AVG(QFL_EY(0,CT),QFL_EY(0,FY1),QFL_EY(0,FY2))',
#  'Value - OCFY': 'AVG(QFL_OCFY(0,CT),QFL_OCFY(0,FY1),QFL_OCFY(0,FY2))',
#  'Value - FCFY': 'AVG(QFL_FCFY(0,CT),QFL_FCFY(0,FY1),QFL_FCFY(0,FY2))',
#  'Value - BP': 'AVG(QFL_BP(0,CT),QFL_BP(0,FY1),QFL_BP(0,FY2))',
#  'Value - TBP': 'AVG(QFL_TBP(0,CT),QFL_TBP(0,FY1),QFL_TBP(0,FY2))',
#  'Value - SP': 'AVG(QFL_SP(0,CT),QFL_SP(0,FY1),QFL_SP(0,FY2))',
#  'Value - EBITDA_EV': 'AVG(QFL_EBITDAEV(0,CT),QFL_EBITDAEV(0,FY1),QFL_EBITDAEV(0,FY2))',
#  'Value - EBIT_EV': 'AVG(QFL_EBITDAEV(0,CT),QFL_EBITDAEV(0,FY1),QFL_EBITDAEV(0,FY2))',
#  'Value - EBITDACAPEX_EV': 'AVG(QFL_EBITDACAPEXEV(0,CT),QFL_EBITDACAPEXEV(0,FY1),QFL_EBITDACAPEXEV(0,FY2))',
#  'Value - IC_EV': 'AVG(QFL_ICEV(0,CT),QFL_ICEV(0,FY1),QFL_ICEV(0,FY2))',
#  'Value - REV_EV': 'AVG(QFL_REVEV(0,CT),QFL_REVEV(0,FY1),QFL_REVEV(0,FY2))',
#  'Value - PEG': 'AVG(QFL_PEG(0,CT),QFL_PEG(0,FY1),QFL_PEG(0,FY2))',
#  'Value - PEGY': 'AVG(QFL_PEGY(0,CT),QFL_PEGY(0,FY1),QFL_PEGY(0,FY2))',
#  'Growth & Sentiment - LTG': 'QFL_LTG(0)',
#  'Growth & Sentiment - STABLE_SALES_GR': 'QFL_STABLE_SALES_GR(0)',
#  'Growth & Sentiment - STABLE_EBIT_GR': 'QFL_STABLE_EBIT_GR(0)',
#  'Growth & Sentiment - STABLE_EBITDA_GR': 'QFL_STABLE_EBITDA_GR(0)',
#  'Growth & Sentiment - STABLE_NET_INC_GR': 'QFL_STABLE_NET_INC_GR(0)',
#  'Growth & Sentiment - STABLE_EPS_GR': 'QFL_STABLE_EPS_GR(0)',
#  'Growth & Sentiment - STABLE_OCF_GR': 'QFL_STABLE_OCF_GR(0)',
#  'Growth & Sentiment - STABLE_FCF_GR': 'QFL_STABLE_FCF_GR(0)',
#  'Growth & Sentiment - STABLE_DPS_GR': 'QFL_STABLE_DPS_GR(0)',
#  'Growth & Sentiment - RD_SALES': 'AVG(QFL_RD_SALES(0,CT),QFL_RD_SALES(0,FY1),QFL_RD_SALES(0,FY2))',
#  'Growth & Sentiment - RD_BV': 'AVG(QFL_RD_BV(0,CT),QFL_RD_BV(0,FY1),QFL_RD_BV(0,FY2))',
#  'Growth & Sentiment - RD_MV': 'AVG(QFL_RD_MV(0,CT),QFL_RD_MV(0,FY1),QFL_RD_MV(0,FY2))',
#  'Growth & Sentiment - CFI_SALES': 'AVG(QFL_CFI_SALES(0,CT),QFL_CFI_SALES(0,FY1),QFL_CFI_SALES(0,FY2))',
#  'Growth & Sentiment - CFI_BV': 'AVG(QFL_CFI_BV(0,CT),QFL_CFI_BV(0,FY1),QFL_CFI_BV(0,FY2))',
#  'Growth & Sentiment - CFI_MV': 'AVG(QFL_CFI_MV(0,CT),QFL_CFI_MV(0,FY1),QFL_CFI_MV(0,FY2))',
#  'Growth & Sentiment - RET_RATIO': 'AVG(QFL_RET_RATIO(0,CT),QFL_RET_RATIO(0,FY1),QFL_RET_RATIO(0,FY2))',
#  'Growth & Sentiment - SALES_EST_REV': 'AVG(QFL_SALES_EST_REV(0,45D),QFL_SALES_EST_REV(0,75D))',
#  'Growth & Sentiment - OCF_EST_REV': 'AVG(QFL_OCF_EST_REV(0,45D),QFL_OCF_EST_REV(0,75D))',
#  'Growth & Sentiment - FCF_EST_REV': 'AVG(QFL_FCF_EST_REV(0,45D),QFL_FCF_EST_REV(0,75))',
#  'Growth & Sentiment - EBIT_EST_REV': 'AVG(QFL_EBIT_EST_REV(0,45D),QFL_EBIT_EST_REV(0,75))',
#  'Growth & Sentiment - EBITDA_EST_REV': 'AVG(QFL_EBITDA_EST_REV(0,45D),QFL_EBITDA_EST_REV(0,75))',
#  'Growth & Sentiment - EPS_EST_REV': 'AVG(QFL_EPS_EST_REV(0,45D),QFL_EPS_EST_REV(0,75))',
#  'Growth & Sentiment - PTGT_EST_REV': 'AVG(QFL_PTGT_EST_REV(0,45D),QFL_PTGT_EST_REV(0,75))',
#  'Growth & Sentiment - SALES_STABLE_EST': 'QFL_SALES_STABLE_EST(0)',
#  'Growth & Sentiment - OCF_STABLE_EST': 'QFL_OCF_STABLE_EST(0)',
#  'Growth & Sentiment - FCF_STABLE_EST': 'QFL_FCF_STABLE_EST(0)',
#  'Growth & Sentiment - EBIT_STABLE_EST': 'QFL_EBIT_STABLE_EST(0)',
#  'Growth & Sentiment - EBITDA_STABLE_EST': 'QFL_EBITDA_STABLE_EST(0)',
#  'Growth & Sentiment - EPS_STABLE_EST': 'QFL_EPS_STABLE_EST(0)',
#  'Growth & Sentiment - PTGT_STABLE_EST': 'QFL_PTGT_STABLE_EST(0)',
#  'Growth & Sentiment - SAPT': 'QFL_SAPT(0)',
#  'Growth & Sentiment - ROBUST_EST_REV': 'AVG(QFL_ROBUST_EST_REV(0,45D),QFL_ROBUST_EST_REV(0,75D))',
#  'Quality - ACCRUALS_BS': 'QFL_ACCRUALS_BS(0)',
#  'Quality - ACCRUALS_CF': 'QFL_ACCRUALS_CF(0)',
#  'Quality - CASH_GEN_PWR': 'QFL_CASH_GEN_PWR(0)',
#  'Quality - EFDR': 'QFL_EFDR(0)',
#  'Quality - EFR': 'QFL_EFR(0)',
#  'Quality - OCF_EARNINGS': 'QFL_OCF_EARNINGS(0)',
#  'Quality - OCF_EARNINGS_VAR': 'QFL_OCF_EARNINGS_VAR(0)',
#  'Quality - DPS_VAR': 'QFL_DPS_VAR(0)',
#  'Quality - ACCUM_DEPR_RATIO': 'QFL_ACCUM_DEPR_RATIO(0)',
#  'Quality - ASSET_LIFE': 'QFL_ASSET_LIFE(0)',
#  'Quality - DFD_REV_CHG_SALES': 'QFL_DFD_REV_CHG_SALES(0)',
#  'Quality - AR_CHG_SALES': 'QFL_AR_CHG_SALES(0)',
#  'Quality - DFD_TAX_CHG_SALES': 'QFL_DFD_TAX_CHG_SALES(0)',
#  'Quality - PREP_EXP_CHG_SALES': 'QFL_PREP_EXP_CHG_SALES(0)',
#  'Quality - INTANG_CHG_SALES': 'QFL_INTANG_CHG_SALES(0)',
#  'Quality - CASH_REV_SALES': 'QFL_CASH_REV_SALES(0)',
#  'Quality - AR_SALES': 'QFL_AR_SALES(0)',
#  'Quality - DFD_TAX_SALES': 'QFL_DFD_TAX_SALES(0)',
#  'Quality - PREP_EXP_SALES': 'QFL_PREP_EXP_SALES(0)',
#  'Quality - INTANG_SALES': 'QFL_INTANG_SALES(0)',
#  'Quality - PREP_EXP_INVEN': 'QFL_PREP_EXP_INVEN(0,LEVEL)',
#  'Quality - PREP_EXP_INVEN_CHG': 'QFL_PREP_EXP_INVEN(0,CHANGE)',
#  'Quality - FG_INVEN': 'QFL_FG_INVEN(0,LEVEL)',
#  'Quality - FG_INVEN_CHG': 'QFL_FG_INVEN(0,CHANGE)',
#  'Quality - BDEBT_AR': 'QFL_BDEBT_AR(0,LEVEL)',
#  'Quality - BDEBT_AR_CHG': 'QFL_BDEBT_AR(0,CHANGE)',
#  'Quality - MIN_INT_EQ': 'QFL_MIN_INT_EQ(0,LEVEL)',
#  'Quality - MIN_INT_EQ_CHG': 'QFL_MIN_INT_EQ(0,CHANGE)',
#  'Quality - SALES_STABILITY': 'QFL_SALES_STABILITY(0)',
#  'Quality - EBIT_STABILITY': 'QFL_EBIT_STABILITY(0)',
#  'Quality - EBITDA_STABILITY': 'QFL_EBITDA_STABILITY(0)',
#  'Quality - OCF_STABILITY': 'QFL_OCF_STABILITY(0)',
#  'Quality - FCF_STABILITY': 'QFL_FCF_STABILITY(0)',
#  'Quality - EPS_STABILITY': 'QFL_EPS_STABILITY(0)',
#  'Quality - NET_INC_STABILITY': 'QFL_NET_INC_STABILITY(0)',
#  'Quality - GROSS_MGN_STABILITY': 'QFL_GROSS_MGN_STABILITY(0)',
#  'Quality - EBIT_MGN_STABILITY': 'QFL_EBIT_MGN_STABILITY(0)',
#  'Quality - EBITDA_MGN_STABILITY': 'QFL_EBITDA_MGN_STABILITY(0)',
#  'Quality - OCF_MGN_STABILITY': 'QFL_OCF_MGN_STABILITY(0)',
#  'Quality - FCF_MGN_STABILITY': 'QFL_FCF_MGN_STABILITY(0)',
#  'Quality - PTX_MGN_STABILITY': 'QFL_PTX_MGN_STABILITY(0)',
#  'Quality - NET_MGN_STABILITY': 'QFL_NET_MGN_STABILITY(0)',
#  'Quality - PIOTROSKI_F': 'QFL_PIOTROSKI_F(0)',
#  'Quality - BENEISH_M': 'QFL_BENEISH_M(0)',
#  'Quality - ALTMAN_Z': 'QFL_ALTMAN_Z(0)',
#  'Profitability & Efficiency - ROA': 'AVG(QFL_ROA(0,CT),QFL_ROA(0,FY1),QFL_ROA(0,FY2))',
#  'Profitability & Efficiency - ROIC': 'AVG(QFL_ROIC(0,CT),QFL_ROIC(0,FY1),QFL_ROIC(0,FY2))',
#  'Profitability & Efficiency - ROTC': 'AVG(QFL_ROTC(0,CT),QFL_ROTC(0,FY1),QFL_ROTC(0,FY2))',
#  'Profitability & Efficiency - ROCE': 'AVG(QFL_ROCE(0,CT),QFL_ROCE(0,FY1),QFL_ROCE(0,FY2))',
#  'Profitability & Efficiency - ROCEQ': 'QFL_ROCEQ(0)',
#  'Profitability & Efficiency - ROE': 'AVG(QFL_ROE(0,CT),QFL_ROE(0,FY1),QFL_ROE(0,FY2))',
#  'Profitability & Efficiency - ROTE': 'AVG(QFL_ROTE(0,CT),QFL_ROTE(0,FY1),QFL_ROTE(0,FY2))',
#  'Profitability & Efficiency - CFROA': 'AVG(QFL_CFROA(0,CT),QFL_CFROA(0,FY1),QFL_CFROA(0,FY2))',
#  'Profitability & Efficiency - CFROE': 'AVG(QFL_CFROE(0,CT),QFL_CFROE(0,FY1),QFL_CFROE(0,FY2))',
#  'Profitability & Efficiency - CFROIC': 'AVG(QFL_CFROIC(0,CT),QFL_CFROIC(0,FY1),QFL_CFROIC(0,FY2))',
#  'Profitability & Efficiency - CFPPE': 'QFL_CFPPE(0)',
#  'Profitability & Efficiency - GROSS_MGN': 'AVG(QFL_GROSS_MGN(0,CT),QFL_GROSS_MGN(0,FY1),QFL_GROSS_MGN(0,FY2))',
#  'Profitability & Efficiency - OPER_MGN': 'QFL_OPER_MGN(0)',
#  'Profitability & Efficiency - EBIT_MGN': 'AVG(QFL_EBIT_MGN(0,CT),QFL_EBIT_MGN(0,FY1),QFL_EBIT_MGN(0,FY2))',
#  'Profitability & Efficiency - EBITDA_MGN': 'AVG(QFL_EBITDA_MGN(0,CT),QFL_EBITDA_MGN(0,FY1),QFL_EBITDA_MGN(0,FY2))',
#  'Profitability & Efficiency - PTX_MGN': 'AVG(QFL_PTX_MGN(0,CT),QFL_PTX_MGN(0,FY1),QFL_PTX_MGN(0,FY2))',
#  'Profitability & Efficiency - OCF_MGN': 'AVG(QFL_OCF_MGN(0,CT),QFL_OCF_MGN(0,FY1),QFL_OCF_MGN(0,FY2))',
#  'Profitability & Efficiency - FCF_MGN': 'AVG(QFL_FCF_MGN(0,CT),QFL_FCF_MGN(0,FY1),QFL_FCF_MGN(0,FY2))',
#  'Profitability & Efficiency - NET_MGN': 'AVG(QFL_NET_MGN(0,CT),QFL_NET_MGN(0,FY1),QFL_NET_MGN(0,FY2))',
#  'Profitability & Efficiency - SGA_SALES': 'AVG(QFL_SGA_SALES(0,CT),QFL_SGA_SALES(0,FY1),QFL_SGA_SALES(0,FY2))',
#  'Profitability & Efficiency - ASSET_TURN': 'AVG(QFL_ASSET_TURN(0,CT),QFL_ASSET_TURN(0,FY1),QFL_ASSET_TURN(0,FY2))',
#  'Profitability & Efficiency - FIXED_ASSET_TURN': 'QFL_FIXED_ASSET_TURN(0)',
#  'Profitability & Efficiency - RECEIV_TURN': 'AVG(QFL_RECEIV_TURN(0,CT),QFL_RECEIV_TURN(0,FY1),QFL_RECEIV_TURN(0,FY2))',
#  'Profitability & Efficiency - PAY_TURN': 'AVG(QFL_PAY_TURN(0,CT),QFL_PAY_TURN(0,FY1),QFL_PAY_TURN(0,FY2))',
#  'Profitability & Efficiency - WKCAP_TURN': 'AVG(QFL_WKCAP_TURN(0,CT),QFL_WKCAP_TURN(0,FY1),QFL_WKCAP_TURN(0,FY2))',
#  'Profitability & Efficiency - INVEN_TURN': 'AVG(QFL_INVEN_TURN(0,CT),QFL_INVEN_TURN(0,FY1),QFL_INVEN_TURN(0,FY2))',
#  'Profitability & Efficiency - EQUITY_TURN': 'AVG(QFL_EQUITY_TURN(0,CT),QFL_EQUITY_TURN(0,FY1),QFL_EQUITY_TURN(0,FY2))',
#  'Profitability & Efficiency - DIO': 'AVG(QFL_DIO(0,CT),QFL_DIO(0,FY1),QFL_DIO(0,FY2))',
#  'Profitability & Efficiency - DSO': 'AVG(QFL_DSO(0,CT),QFL_DSO(0,FY1),QFL_DSO(0,FY2))',
#  'Profitability & Efficiency - DPO': 'AVG(QFL_DPO(0,CT),QFL_DPO(0,FY1),QFL_DPO(0,FY2))',
#  'Profitability & Efficiency - CCC': 'AVG(QFL_CCC(0,CT),QFL_CCC(0,FY1),QFL_CCC(0,FY2))',
#  'Profitability & Efficiency - INVEN_SALES': 'AVG(QFL_INVEN_SALES(0,CT),QFL_INVEN_SALES(0,FY1),QFL_INVEN_SALES(0,FY2))',
#  'Profitability & Efficiency - CF_EMP': 'AVG(QFL_CF_EMP(0,CT),QFL_CF_EMP(0,FY1),QFL_CF_EMP(0,FY2))',
#  'Profitability & Efficiency - REV_EMP': 'AVG(QFL_REV_EMP(0,CT),QFL_REV_EMP(0,FY1),QFL_REV_EMP(0,FY2))',
#  'Profitability & Efficiency - NI_EMP': 'AVG(QFL_NI_EMP(0,CT),QFL_NI_EMP(0,FY1),QFL_NI_EMP(0,FY2))',
#  'Profitability & Efficiency - ASSETS_EMP': 'AVG(QFL_ASSETS_EMP(0,CT),QFL_ASSETS_EMP(0,FY1),QFL_ASSETS_EMP(0,FY2))',
#  'Solvency - CURR_RATIO': 'AVG(QFL_CURR_RATIO(0,CT),QFL_CURR_RATIO(0,FY1),QFL_CURR_RATIO(0,FY2))',
#  'Solvency - QUICK_RATIO': 'AVG(QFL_QUICK_RATIO(0,CT),QFL_QUICK_RATIO(0,FY1),QFL_QUICK_RATIO(0,FY2))',
#  'Solvency - CURR_ASSET_LIQ': 'AVG(QFL_CURR_ASSET_LIQ(0,CT),QFL_CURR_ASSET_LIQ(0,FY1),QFL_CURR_ASSET_LIQ(0,FY2))',
#  'Solvency - CASH_RATIO': 'AVG(QFL_CASH_RATIO(0,CT),QFL_CASH_RATIO(0,FY1),QFL_CASH_RATIO(0,FY2))',
#  'Solvency - DEFENSE_RATIO': 'AVG(QFL_DEFENSE_RATIO(0,CT),QFL_DEFENSE_RATIO(0,FY1),QFL_DEFENSE_RATIO(0,FY2))',
#  'Solvency - ST_DEBT_ASSETS': 'AVG(QFL_ST_DEBT_ASSETS(0,CT),QFL_ST_DEBT_ASSETS(0,FY1),QFL_ST_DEBT_ASSETS(0,FY2))',
#  'Solvency - LT_DEBT_ASSETS': 'AVG(QFL_LT_DEBT_ASSETS(0,CT),QFL_LT_DEBT_ASSETS(0,FY1),QFL_LT_DEBT_ASSETS(0,FY2))',
#  'Solvency - DEBT_ASSETS': 'AVG(QFL_DEBT_ASSETS(0,CT),QFL_DEBT_ASSETS(0,FY1),QFL_DEBT_ASSETS(0,FY2))',
#  'Solvency - ST_DEBT_CAPITAL': 'AVG(QFL_ST_DEBT_CAPITAL(0,CT),QFL_ST_DEBT_CAPITAL(0,FY1),QFL_ST_DEBT_CAPITAL(0,FY2))',
#  'Solvency - LT_DEBT_CAPITAL': 'AVG(QFL_LT_DEBT_CAPITAL(0,CT),QFL_LT_DEBT_CAPITAL(0,FY1),QFL_LT_DEBT_CAPITAL(0,FY2))',
#  'Solvency - DEBT_CAPITAL': 'AVG(QFL_DEBT_CAPITAL(0,CT),QFL_DEBT_CAPITAL(0,FY1),QFL_DEBT_CAPITAL(0,FY2))',
#  'Solvency - ST_DEBT_EQUITY': 'AVG(QFL_ST_DEBT_EQUITY(0,CT),QFL_ST_DEBT_EQUITY(0,FY1),QFL_ST_DEBT_EQUITY(0,FY2))',
#  'Solvency - LT_DEBT_EQUITY': 'AVG(QFL_LT_DEBT_EQUITY(0,CT),QFL_LT_DEBT_EQUITY(0,FY1),QFL_LT_DEBT_EQUITY(0,FY2))',
#  'Solvency - DEBT_EQUITY': 'AVG(QFL_DEBT_EQUITY(0,CT),QFL_DEBT_EQUITY(0,FY1),QFL_DEBT_EQUITY(0,FY2))',
#  'Solvency - LEVERAGE': 'AVG(QFL_LEVERAGE(0,CT),QFL_LEVERAGE(0,FY1),QFL_LEVERAGE(0,FY2))',
#  'Solvency - INT_COV': 'AVG(QFL_INT_COV(0,CT),QFL_INT_COV(0,FY1),QFL_INT_COV(0,FY2))',
#  'Solvency - FIX_CHRG_COV': 'QFL_FIX_CHRG_COV(0)',
#  'Solvency - LIAB_FCF_COV': 'AVG(QFL_LIAB_FCF_COV(0,CT),QFL_LIAB_FCF_COV(0,FY1),QFL_LIAB_FCF_COV(0,FY2))',
#  'Solvency - LIAB_COV': 'AVG(QFL_LIAB_COV(0,CT),QFL_LIAB_COV(0,FY1),QFL_LIAB_COV(0,FY2))',
#  'Solvency - CURR_LIAB_FCF_COV': 'AVG(QFL_CURR_LIAB_FCF_COV(0,CT),QFL_CURR_LIAB_FCF_COV(0,FY1),QFL_CURR_LIAB_FCF_COV(0,FY2))',
#  'Solvency - CURR_LIAB_COV': 'AVG(QFL_CURR_LIAB_COV(0,CT),QFL_CURR_LIAB_COV(0,FY1),QFL_CURR_LIAB_COV(0,FY2))',
#  'Solvency - CASH_COV': 'AVG(QFL_CASH_COV(0,CT),QFL_CASH_COV(0,FY1),QFL_CASH_COV(0,FY2))',
#  'Solvency - DEBT_SVC_RATIO': 'AVG(QFL_DEBT_SVC_RATIO(0,CT),QFL_DEBT_SVC_RATIO(0,FY1),QFL_DEBT_SVC_RATIO(0,FY2))',
#  'Solvency - ASSET_COV': 'AVG(QFL_ASSET_COV(0,CT),QFL_ASSET_COV(0,FY1),QFL_ASSET_COV(0,FY2))',
#  'Solvency - CAPEX_COV': 'AVG(QFL_CAPEX_COV(0,CT),QFL_CAPEX_COV(0,FY1),QFL_CAPEX_COV(0,FY2))',
#  'Solvency - DIV_COV': 'AVG(QFL_DIV_COV(0,CT),QFL_DIV_COV(0,FY1),QFL_DIV_COV(0,FY2))',
#  'Solvency - ST_DEBT_PCT': 'AVG(QFL_ST_DEBT_PCT(0,CT),QFL_ST_DEBT_PCT(0,FY1),QFL_ST_DEBT_PCT(0,FY2))',
#  'Management & Corp Gov - ASSET_GR': 'QFL_ASSET_GR(0,LT)',
#  'Management & Corp Gov - CAPEX_GR': 'QFL_CAPEX_GR(0,LT)',
#  'Management & Corp Gov - DEBT_ISS_GR': 'QFL_DEBT_ISS_GR(0,LT)',
#  'Management & Corp Gov - EQUITY_ISS_GR': 'QFL_EQUITY_ISS_GR(0,LT)',
#  'Management & Corp Gov - EQ_BUYBACK_RATIO': 'QFL_EQ_BUYBACK_RATIO(0)',
#  'Management & Corp Gov - EPS_MGMT': 'QFL_EPS_MGMT(0,CT)',
#  'Management & Corp Gov - DEP_AMORT_RATIO': 'QFL_DEP_AMORT_RATIO(0)',
#  'Management & Corp Gov - DEP_AMORT_VAR': 'QFL_DEP_AMORT_VAR(0)',
#  'Management & Corp Gov - CAPEX_DEPR': 'QFL_CAPEX_DEPR(0,CT)',
#  'Management & Corp Gov - MGMT_CONNECTIONS': 'QFL_MGMT_CONNECTIONS(0)',
#  'Management & Corp Gov - MGMT_TENURE': 'QFL_MGMT_TENURE(0,AVG)',
#  'Management & Corp Gov - MGMT_COMP_AVG': 'QFL_MGMT_COMP_AVG(0)',
#  'Management & Corp Gov - MGMT_FEMALE_CEO': 'QFL_MGMT_FEMALE_CEO(0)',
#  'Management & Corp Gov - MGMT_FOUNDER_LED': 'QFL_MGMT_FOUNDER_LED(0)',
#  'Management & Corp Gov - MGMT_CEO_CHAIR': 'QFL_MGMT_CEO_CHAIR(0)',
#  'Management & Corp Gov - BRD_NUM_OTH_BRD': 'QFL_BRD_NUM_OTH_BRD(0) / QFL_BRD_NUM_TOT(0)',
#  'Management & Corp Gov - BRD_NUM_IND': 'QFL_BRD_NUM_IND(0) / QFL_BRD_NUM_TOT(0)',
#  'Management & Corp Gov - BRD_NUM_FEM': 'QFL_BRD_NUM_FEM(0) / QFL_BRD_NUM_TOT(0)',
#  'Management & Corp Gov - BRD_ACTIVIST': 'QFL_BRD_ACTIVIST(0)',
#  'Management & Corp Gov - BRD_PEVC': 'QFL_BRD_PEVC(0)',
#  'Management & Corp Gov - BRD_FEMALE_CHAIR': 'QFL_BRD_FEMALE_CHAIR(0)',
#  'Management & Corp Gov - BRD_TENURE': 'QFL_BRD_TENURE(0,AVG)',
#  'Crowding & Insider Activity - PASSIVE_PCTOUT': 'QFL_PASSIVE_PCTOUT(0)',
#  'Crowding & Insider Activity - PASSIVE_PCPRT': 'QFL_PASSIVE_PCPRT(0)',
#  'Crowding & Insider Activity - PASSIVE_CONC': 'QFL_PASSIVE_CONC(0)',
#  'Crowding & Insider Activity - PASSIVE_VOTES_PCT': 'QFL_PASSIVE_VOTES_PCT(0)',
#  'Crowding & Insider Activity - ACTIVE_PCTOUT': 'QFL_ACTIVE_PCTOUT(0)',
#  'Crowding & Insider Activity - ACTIVE_PCPRT': 'QFL_ACTIVE_PCPRT(0)',
#  'Crowding & Insider Activity - ACTIVE_CONC': 'QFL_ACTIVE_CONC(0)',
#  'Crowding & Insider Activity - ACTIVE_VOTES_PCT': 'QFL_ACTIVE_VOTES_PCT(0)',
#  'Crowding & Insider Activity - INSTIT_PCTOUT': 'QFL_INSTIT_PCTOUT(0)',
#  'Crowding & Insider Activity - INSTIT_PCPRT': 'QFL_INSTIT_PCPRT(0)',
#  'Crowding & Insider Activity - INSTIT_CONC': 'QFL_INSTIT_CONC(0)',
#  'Crowding & Insider Activity - INSTIT_VOTES_PCT': 'QFL_INSTIT_VOTES_PCT(0)',
#  'Crowding & Insider Activity - ETF_PCTOUT': 'QFL_ETF_PCTOUT(0)',
#  'Crowding & Insider Activity - ETF_PCPRT': 'QFL_ETF_PCPRT(0)',
#  'Crowding & Insider Activity - ETF_CONC': 'QFL_ETF_CONC(0)',
#  'Crowding & Insider Activity - ETF_VOTES_PCT': 'QFL_ETF_VOTES_PCT(0)',
#  'Crowding & Insider Activity - HF_PCTOUT': 'QFL_HF_PCTOUT(0)',
#  'Crowding & Insider Activity - HF_PCPRT': 'QFL_HF_PCPRT(0)',
#  'Crowding & Insider Activity - HF_CONC': 'QFL_HF_CONC(0)',
#  'Crowding & Insider Activity - HF_VOTES_PCT': 'QFL_HF_VOTES_PCT(0)',
#  'Crowding & Insider Activity - INSIDER_HLDRS': 'QFL_INSIDER_HLDRS(0)',
#  'Crowding & Insider Activity - INSIDER_PCTOUT': 'QFL_INSIDER_PCTOUT(0)',
#  'Crowding & Insider Activity - INSIDER_NUM_BUYS': 'AVG(QFL_INSIDER_NUM_BUYS(0,1M),QFL_INSIDER_NUM_BUYS(0,3M),QFL_INSIDER_NUM_BUYS(0,6M),QFL_INSIDER_NUM_BUYS(0,12M))',
#  'Crowding & Insider Activity - INSIDER_NUM_SELLS': 'AVG(QFL_INSIDER_NUM_SELLS(0,1M),QFL_INSIDER_NUM_SELLS(0,3M),QFL_INSIDER_NUM_SELLS(0,6M),QFL_INSIDER_NUM_SELLS(0,12M))',
#  'Crowding & Insider Activity - INSIDER_BUYER_CHG': 'ZAV(AVG((QFL_INSIDER_BUYER_POSCHG(0,1M)/(QFL_INSIDER_BUYER_POS(0,1M)-QFL_INSIDER_BUYER_POSCHG(0,1M))),(QFL_INSIDER_BUYER_POSCHG(0,3M)/(QFL_INSIDER_BUYER_POS(0,3M)-QFL_INSIDER_BUYER_POSCHG(0,3M))),(QFL_INSIDER_BUYER_POSCHG(0,6M)/(QFL_INSIDER_BUYER_POS(0,6M)-QFL_INSIDER_BUYER_POSCHG(0,6M))),(QFL_INSIDER_BUYER_POSCHG(0,12M)/(QFL_INSIDER_BUYER_POS(0,12M)-QFL_INSIDER_BUYER_POSCHG(0,12M)))))',
#  'Crowding & Insider Activity - INSIDER_SELLER_CHG': 'ZAV(AVG((QFL_INSIDER_SELLER_POSCHG(0,1M)/(QFL_INSIDER_SELLER_POS(0,1M)-QFL_INSIDER_SELLER_POSCHG(0,1M))),(QFL_INSIDER_SELLER_POSCHG(0,3M)/(QFL_INSIDER_SELLER_POS(0,3M)-QFL_INSIDER_SELLER_POSCHG(0,3M))),(QFL_INSIDER_SELLER_POSCHG(0,6M)/(QFL_INSIDER_SELLER_POS(0,6M)-QFL_INSIDER_SELLER_POSCHG(0,6M))),(QFL_INSIDER_SELLER_POSCHG(0,12M)/(QFL_INSIDER_SELLER_POS(0,12M)-QFL_INSIDER_SELLER_POSCHG(0,12M)))))',
#  # 'Crowding & Insider Activity - INSIDER_CHG': 'ZAV(AVG((QFL_INSIDER_BUYS(0,1M)-QFL_INSIDER_SELLS(0,1M))/MAX(0,(QFL_INSIDER_POS(0)-(QFL_INSIDER_BUYS(0,1M)-QFL_INSIDER_SELLS(0,1M)))),(QFL_INSIDER_BUYS(0,3M)-QFL_INSIDER_SELLS(0,3M))/MAX(0,(QFL_INSIDER_POS(0)-(QFL_INSIDER_BUYS(0,3M)-QFL_INSIDER_SELLS(0,3M)))),(QFL_INSIDER_BUYS(0,6M)-QFL_INSIDER_SELLS(0,6M))/MAX(0,(QFL_INSIDER_POS(0)-(QFL_INSIDER_BUYS(0,6M)-QFL_INSIDER_SELLS(0,6M)))),(QFL_INSIDER_BUYS(0,12M)-QFL_INSIDER_SELLS(0,12M))/MAX(0,(QFL_INSIDER_POS(0)-(QFL_INSIDER_BUYS(0,12M)-QFL_INSIDER_SELLS(0,12M))))))',
#  'Market - ST_RES_MOM': 'AVG(QFL_RES_RET_MOM(0,21D),QFL_RES_RET_MOM(0,63D))',
#  'Market - LT_RES_MOM': 'AVG(QFL_RES_RET_MOM(0,252D),QFL_RES_RET_MOM(0,36M),QFL_RES_RET_MOM(0,60M))',
#  'Market - ST_RET_MOM': 'AVG(QFL_RET_MOM(0,21D),QFL_RET_MOM(0,63D))',
#  'Market - LT_RET_MOM': 'AVG(QFL_RET_MOM(0,252D),QFL_RET_MOM(0,36M),QFL_RET_MOM(0,60M))',
#  'Market - ST_STOCHASTIC': 'AVG(QFL_STOCHASTIC(0,21D),QFL_STOCHASTIC(0,63D))',
#  'Market - LT_STOCHASTIC': 'AVG(QFL_STOCHASTIC(0,252D),QFL_STOCHASTIC(0,36M),QFL_STOCHASTIC(0,60M))',
#  'Market - ST_RSI': 'AVG(QFL_RSI(0,21D),QFL_RSI(0,63D))',
#  'Market - LT_RSI': 'AVG(QFL_RSI(0,252D),QFL_RSI(0,36M),QFL_RSI(0,60M))',
#  'Market - ST_ACCEL': 'AVG(QFL_ACCEL(0,21D),QFL_ACCEL(0,63D))',
#  'Market - LT_ACCEL': 'AVG(QFL_ACCEL(0,252D),QFL_ACCEL(0,36M),QFL_ACCEL(0,60M))',
#  'Market - ST_VELOCITY': 'AVG(QFL_VELOCITY(0,21D),QFL_VELOCITY(0,63D))',
#  'Market - LT_VELOCITY': 'AVG(QFL_VELOCITY(0,252D),QFL_VELOCITY(0,36M),QFL_VELOCITY(0,60M))',
#  'Market - 52W': 'QFL_POS52W(0)',
#  'Market - ST_RES_VOL': 'AVG(QFL_RES_RET_VOL(0,21D),QFL_RES_RET_VOL(0,63D))',
#  'Market - LT_RES_VOL': 'AVG(QFL_RES_RET_VOL(0,252D),QFL_RES_RET_VOL(0,36M),QFL_RES_RET_VOL(0,60M))',
#  'Market - ST_RET_VOL': 'AVG(QFL_RET_VOL(0,21D),QFL_RET_VOL(0,63D))',
#  'Market - LT_RET_VOL': 'AVG(QFL_RET_VOL(0,252D),QFL_RET_VOL(0,36M),QFL_RET_VOL(0,60M))',
#  'Market - ST_SKEW': 'AVG(QFL_SKEW(0,21D),QFL_SKEW(0,63D))',
#  'Market - LT_SKEW': 'AVG(QFL_SKEW(0,252D),QFL_SKEW(0,36M),QFL_SKEW(0,60M))',
#  'Market - ST_TURBULENCE': 'AVG(QFL_TURBULENCE(0,21D),QFL_TURBULENCE(0,63D))',
#  'Market - LT_TURBULENCE': 'AVG(QFL_TURBULENCE(0,252D),QFL_TURBULENCE(0,36M),QFL_TURBULENCE(0,60M))',
#  'Market - ST_KURTOSIS': 'AVG(QFL_KURTOSIS(0,21D),QFL_KURTOSIS(0,63D))',
#  'Market - LT_KURTOSIS': 'AVG(QFL_KURTOSIS(0,252D),QFL_KURTOSIS(0,36M),QFL_KURTOSIS(0,60M))',
#  'Market - ST_SEMIVARIANCE': 'AVG(QFL_SEMIVARIANCE(0,21D),QFL_SEMIVARIANCE(0,63D))',
#  'Market - LT_SEMIVARIANCE': 'AVG(QFL_SEMIVARIANCE(0,252D),QFL_SEMIVARIANCE(0,36M),QFL_SEMIVARIANCE(0,60M))',
#  'Market - ST_ALPHA': 'AVG(QFL_ALPHA(0,21D),QFL_ALPHA(0,63D))',
#  'Market - LT_ALPHA': 'AVG(QFL_ALPHA(0,252D),QFL_ALPHA(0,36M),QFL_ALPHA(0,60M))',
#  'Market - ST_ATR': 'AVG(QFL_ATR(0,21D),QFL_ATR(0,63D))',
#  'Market - LT_ATR': 'AVG(QFL_ATR(0,252D),QFL_ATR(0,36M),QFL_ATR(0,60M))',
#  'Market - ST_ULCER': 'AVG(QFL_ULCER(0,21D),QFL_ULCER(0,63D))',
#  'Market - LT_ULCER': 'AVG(QFL_ULCER(0,252D),QFL_ULCER(0,36M),QFL_ULCER(0,60M))',
#  'Market - ST_UPI': 'AVG(QFL_UPI(0,21D),QFL_UPI(0,63D))',
#  'Market - LT_UPI': 'AVG(QFL_UPI(0,252D),QFL_UPI(0,36M),QFL_UPI(0,60M))',
#  'Market - ST_DRAWDOWN': 'AVG(QFL_DRAWDOWN(0,21D),QFL_DRAWDOWN(0,63D))',
#  'Market - LT_DRAWDOWN': 'AVG(QFL_DRAWDOWN(0,252D),QFL_DRAWDOWN(0,36M),QFL_DRAWDOWN(0,60M))',
#  'Market - ST_ADLR': 'AVG(QFL_ADLR(0,21D),QFL_ADLR(0,63D))',
#  'Market - LT_ADLR': 'AVG(QFL_ADLR(0,252D),QFL_ADLR(0,36M),QFL_ADLR(0,60M))',
#  'Market - ST_OBVR': 'AVG(QFL_OBVR(0,21D),QFL_OBVR(0,63D))',
#  'Market - LT_OBVR': 'AVG(QFL_OBVR(0,252D),QFL_OBVR(0,36M),QFL_OBVR(0,60M))',
#  'Market - ADT': 'AVG(QFL_ADT(0,21D),QFL_ADT(0,63D),QFL_ADT(0,252D))',
#  'Market - MDT': 'AVG(QFL_MDT(0,21D),QFL_MDT(0,63D),QFL_MDT(0,252D))',
#  'Market - SHARETURN': 'AVG(QFL_SHARETURN(0,21D),QFL_SHARETURN(0,63D),QFL_SHARETURN(0,252D))',
#  'Market - ATVR': 'AVG(QFL_ATVR(0,21D),QFL_ATVR(0,63D),QFL_ATVR(0,252D))',
#  'Market - MTVR': 'AVG(QFL_MTVR(0,21D),QFL_MTVR(0,63D),QFL_MTVR(0,252D))',
#  'Market - LIX': 'QFL_LIX',
#  'Market - ST_BETA': 'AVG(QFL_BETA(0,LEVEL,21D),QFL_BETA(0,LEVEL,63D))',
#  'Market - LT_BETA': 'AVG(QFL_BETA(0,LEVEL,252D),QFL_BETA(0,LEVEL,36M),QFL_BETA(0,LEVEL,60M))',
#  'Market - ST_DOWNBETA': 'AVG(QFL_DOWNBETA(0,LEVEL,21D),QFL_DOWNBETA(0,LEVEL,63D))',
#  'Market - LT_DOWNBETA': 'AVG(QFL_DOWNBETA(0,LEVEL,36M),QFL_DOWNBETA(0,LEVEL,60M),QFL_DOWNBETA(0,LEVEL,252D))',
#  'Market - ST_UPBETA': 'AVG(QFL_UPBETA(0,LEVEL,21D),QFL_UPBETA(0,LEVEL,63D))',
#  'Market - LT_UPBETA': 'AVG(QFL_UPBETA(0,LEVEL,36M),QFL_UPBETA(0,LEVEL,60M),QFL_UPBETA(0,LEVEL,252D))'
    
# }