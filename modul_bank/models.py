from django.db import models


class BaseData(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(
        verbose_name="Дата создания",
        auto_now_add=True
    )

    update_at = models.DateTimeField(
        verbose_name="Дата последнего обновления",
        auto_now=True
    )


class Bank(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название банка',
    )

    class Meta:
        verbose_name = 'Банк'
        verbose_name_plural = 'Банки'

    def __str__(self):
        return self.title


class Company(models.Model):
    bank = models.ForeignKey(
        Bank,
        on_delete=models.CASCADE,
        verbose_name='Банк компании',
        related_name='companies'
    )

    company_id = models.CharField(
        max_length=1000,
        verbose_name='Уникальный id компании',
        unique=True
    )

    company_name = models.CharField(
        max_length=1000,
        verbose_name='Название компании',
    )

    status = models.BooleanField(
        verbose_name='Статус компании'
    )

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __str__(self):
        return self.company_name


class Account(BaseData):
    account_name = models.CharField(
        max_length=500,
        verbose_name='Название счёта'
    )

    balance = models.DecimalField(
        max_digits=19,
        decimal_places=2
    )

    bank_bic = models.CharField(
        max_length=255,
        verbose_name='Бик'
    )

    bank_correspondent_account = models.CharField(
        max_length=300,
        verbose_name='Корреспондентский счёт'
    )

    bank_inn = models.CharField(
        max_length=255,
        verbose_name='Инн'
    )

    bank_kpp = models.CharField(
        max_length=255,
        verbose_name='Кпп'
    )

    begin_date = models.DateTimeField(
        verbose_name='Дата открытия счёта'
    )

    currency = models.CharField(
        max_length=100,
        verbose_name='Валюта счёта'
    )

    id_account = models.CharField(
        max_length=1000,
        verbose_name='Уникальный id cчёта',
        unique=True
    )

    number = models.CharField(
        max_length=255,
        verbose_name='Номер счёта'
    )

    status = models.CharField(
        max_length=255,
        verbose_name='Статус'
    )
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name='accounts'
    )

    class Meta:
        verbose_name = 'Счет'
        verbose_name_plural = 'Счета'

    def __str__(self):
        return f'{self.account_name}-{self.begin_date}'


class Operation(BaseData):
    id_payment = models.CharField(
        max_length=1000,
        verbose_name='Системный идентификатор транзакции',
        unique=True
    )

    card_id = models.CharField(
        max_length=1000,
        blank=True,
        verbose_name='Идентификатор карты, к которой привязан платёж'
    )

    company_id = models.CharField(
        max_length=1000,
        blank=True,
        verbose_name='Системный идентификатор компании'
    )

    status = models.CharField(
        max_length=1000,
        verbose_name='Текущий статус транзакции'
    )

    category = models.CharField(
        max_length=1000,
        blank=True,
        verbose_name='Направление платежа'
    )

    contragent_name = models.CharField(
        max_length=1000,
        blank=True,
        verbose_name='Полное наименование контрагента'
    )

    contragent_inn = models.CharField(
        max_length=1000,
        blank=True,
        verbose_name='ИНН контрагента'
    )

    contragent_kpp = models.CharField(
        max_length=1000,
        blank=True,
        verbose_name='КПП контрагента'
    )

    contragent_bank_account_number = models.CharField(
        max_length=1000,
        blank=True,
        verbose_name='Счёт контрагента'
    )

    contragent_bank_corr_account = models.CharField(
        max_length=1000,
        blank=True,
        verbose_name='Коррсчёт контрагента'
    )

    contragent_bank_name = models.CharField(
        max_length=1000,
        blank=True,
        verbose_name='Наименование банка контрагента'
    )

    contragent_bank_bic = models.CharField(
        max_length=1000,
        blank=True,
        verbose_name='БИК банка контрагента'
    )

    currency = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Код валюты'
    )

    amount = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        verbose_name='Сумма платежа без учета банковской комиссии'
    )

    bank_account_number = models.CharField(
        max_length=1000,
        blank=True,
        verbose_name='Номер банковского счета'
    )

    payment_purpose = models.CharField(
        max_length=1000,
        blank=True,
        verbose_name='Назначение платежа'
    )

    executed = models.CharField(
        max_length=1000,
        blank=True,
        verbose_name='Дата проведения платежа'
    )

    created = models.CharField(
        max_length=1000,
        verbose_name='Дата создания транзакции'
    )

    doc_number = models.CharField(
        max_length=1000,
        blank=True,
        verbose_name='Номер документа'
    )

    abs_id = models.CharField(
        max_length=1000,
        blank=True,
        verbose_name='Идентификатор документа в АБС'
    )

    ibso_id = models.CharField(
        max_length=1000,
        blank=True,
        verbose_name='Идентификатор проводки в АБС'
    )

    kbk = models.CharField(
        max_length=1000,
        blank=True,
        verbose_name='Код бюджетной классификации (104)'
    )

    oktmo = models.CharField(
        max_length=1000,
        blank=True,
        verbose_name='классификатор территорий муниципальных образований(105)'
    )

    payment_basis = models.CharField(
        max_length=1000,
        blank=True,
        verbose_name='Для бюджетных и налог. платежей. Основание платежа (106)'
    )

    tax_code = models.CharField(
        max_length=1000,
        blank=True,
        verbose_name='Налог. период (в случае налог. или бюджетного платежа)'
    )

    tax_doc_num = models.CharField(
        max_length=1000,
        blank=True,
        verbose_name='Для бюджетных и налог. платежей. Номер документа (108)'
    )

    tax_doc_date = models.CharField(
        max_length=1000,
        blank=True,
        verbose_name='Для бюджетных и налоговых платежей. Дата документа (109)'
    )

    payer_status = models.CharField(
        max_length=1000,
        blank=True,
        verbose_name='Для бюджетных и налог. платежей. Статус плательщика(101)'
    )

    uin = models.CharField(
        max_length=1000,
        blank=True,
        verbose_name='Для бюджетных и налог. платежей. Уник. id начисления(22)'
    )

    sbp_oper_id = models.CharField(
        max_length=1000,
        blank=True,
        verbose_name='ID операций C2B платежа по СБП'
    )

    sbp_oper_id_for_refund = models.CharField(
        max_length=1000,
        blank=True,
        verbose_name='ID операции возврата С2B платежa'
    )

    rcv_qrc_id = models.CharField(
        max_length=1000,
        blank=True,
        verbose_name='ID QR-кода СБП'
    )

    account = models.ForeignKey(
        Account,
        blank=True,
        on_delete=models.PROTECT,
        related_name='accounts'
    )

    class Meta:
        verbose_name = 'Операция'
        verbose_name_plural = 'Операции'

    def __str__(self):
        return f'{self.id_payment} -- {self.created} -- {self.account.id}'
