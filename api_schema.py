from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, Field


class AccountSchema(BaseModel):
    """Data structure API Account"""
    account_name: str = Field(alias='accountName')
    balance: Decimal
    bank_bic: str = Field(alias='bankBic')
    bank_correspondent_account: str = Field(alias='bankCorrespondentAccount')
    bank_inn: str = Field(alias='bankInn')
    bank_kpp: str = Field(alias='bankKpp')
    begin_date: datetime = Field(alias='beginDate')
    currency: str
    id_account: str = Field(alias='id')
    number: str
    status: str
    company: int = 1

class AccountInfoSchema(BaseModel):
    """Data structure API Company"""
    company_name: str = Field(alias='companyName')
    company_id: str = Field(alias='companyId')
    status: bool = Field(alias='registrationCompleted')
    account: list[AccountSchema] = Field(alias='bankAccounts')
    bank: int = 1


class OperationSchema(BaseModel):
    """Data structure API operation"""
    id_payment: str = Field(alias='id')
    card_id: str = Field(alias='cardId', default='')
    company_id: str = Field(alias='companyId')
    status: str
    category: str
    contragent_name: str = Field(alias='contragentName')
    contragent_inn: str = Field(alias='contragentInn')
    contragent_kpp: str = Field(alias='contragentKpp')
    contragent_bank_account_number: str = Field(alias='contragentBankAccountNumber')
    contragent_bank_corr_account: str = Field(alias='contragentBankCorrAccount')
    contragent_bank_name: str = Field(alias='contragentBankName')
    contragent_bank_bic: str = Field(alias='contragentBankBic', default='')
    currency: str
    amount: Decimal = Field(alias='amount')
    bank_account_number: str = Field(alias='bankAccountNumber')
    payment_purpose: str = Field(alias='paymentPurpose')
    executed: str = ''
    created: str
    doc_number: str = Field(alias='docNumber')
    abs_id: str = Field(alias='absId')
    ibso_id: str = Field(alias='ibsoId')
    kbk: str
    oktmo: str
    payment_basis: str = Field(alias='paymentBasis')
    tax_code: str = Field(alias='taxCode')
    tax_doc_num: str = Field(alias='taxDocNum')
    tax_doc_date: str = Field(alias='taxDocDate')
    payer_status: str = Field(alias='payerStatus')
    uin: str
    sbp_oper_id: str = Field(alias='sbpOperId')
    sbp_oper_id_for_refund: str = Field(alias='sbpOperIdForRefund')
    rcv_qrc_id: str = Field(alias='rcvQrcId')
    account: int = 1




