# Generated by Django 4.2.9 on 2024-01-23 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Дата последнего обновления')),
                ('account_name', models.CharField(max_length=500, verbose_name='Название счёта')),
                ('balance', models.DecimalField(decimal_places=2, max_digits=19)),
                ('bank_bic', models.CharField(max_length=255, verbose_name='Бик')),
                ('bank_correspondent_account', models.CharField(max_length=300, verbose_name='Корреспондентский счёт')),
                ('bank_inn', models.CharField(max_length=255, verbose_name='Инн')),
                ('bank_kpp', models.CharField(max_length=255, verbose_name='Кпп')),
                ('begin_date', models.DateTimeField(verbose_name='Дата открытия счёта')),
                ('currency', models.CharField(max_length=100, verbose_name='Валюта счёта')),
                ('id_account', models.CharField(max_length=1000, verbose_name='Уникальный id cчёта')),
                ('number', models.CharField(max_length=255, verbose_name='Номер счёта')),
                ('status', models.CharField(max_length=255, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Счет',
                'verbose_name_plural': 'Счета',
            },
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название банка')),
            ],
            options={
                'verbose_name': 'Банк',
                'verbose_name_plural': 'Банки',
            },
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_payment', models.CharField(max_length=1000, unique=True, verbose_name='Системный идентификатор транзакции')),
                ('card_id', models.CharField(blank=True, max_length=1000, verbose_name='Идентификатор карты, к которой привязан платёж')),
                ('company_id', models.CharField(blank=True, max_length=1000, verbose_name='Системный идентификатор компании')),
                ('status', models.CharField(blank=True, max_length=1000, verbose_name='Текущий статус транзакции')),
                ('category', models.CharField(blank=True, max_length=1000, verbose_name='Направление платежа')),
                ('contragent_name', models.CharField(blank=True, max_length=1000, verbose_name='Полное наименование контрагента')),
                ('contragent_inn', models.CharField(blank=True, max_length=1000, verbose_name='ИНН контрагента')),
                ('contragent_kpp', models.CharField(blank=True, max_length=1000, verbose_name='КПП контрагента')),
                ('contragent_bank_account_number', models.CharField(blank=True, max_length=1000, verbose_name='Счёт контрагента')),
                ('contragent_bank_name', models.CharField(blank=True, max_length=1000, verbose_name='Наименование банка контрагента')),
                ('contragent_bank_bic', models.CharField(blank=True, max_length=1000, verbose_name='БИК банка контрагента')),
                ('currency', models.CharField(blank=True, max_length=255, verbose_name='Код валюты')),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=19, verbose_name='Сумма платежа без учета банковской комиссии')),
                ('bank_account_number', models.CharField(blank=True, max_length=1000, verbose_name='Номер банковского счета')),
                ('payment_purpose', models.CharField(blank=True, max_length=1000, verbose_name='Назначение платежа')),
                ('executed', models.CharField(blank=True, max_length=1000, verbose_name='Дата проведения платежа')),
                ('created', models.CharField(blank=True, max_length=1000, verbose_name='Дата создания транзакции')),
                ('doc_number', models.CharField(blank=True, max_length=1000, verbose_name='Номер документа')),
                ('abs_id', models.CharField(blank=True, max_length=1000, verbose_name='Идентификатор документа в АБС')),
                ('ibso_id', models.CharField(blank=True, max_length=1000, verbose_name='Идентификатор проводки в АБС')),
                ('kbk', models.CharField(blank=True, max_length=1000, verbose_name='Код бюджетной классификации (104)')),
                ('oktmo', models.CharField(blank=True, max_length=1000, verbose_name='классификатор территорий муниципальных образований(105)')),
                ('payment_basis', models.CharField(blank=True, max_length=1000, verbose_name='Для бюджетных и налог. платежей. Основание платежа (106)')),
                ('tax_code', models.CharField(blank=True, max_length=1000, verbose_name='Налог. период (в случае налог. или бюджетного платежа)')),
                ('tax_doc_num', models.CharField(blank=True, max_length=1000, verbose_name='Для бюджетных и налог. платежей. Номер документа (108)')),
                ('tax_doc_date', models.CharField(blank=True, max_length=1000, verbose_name='Для бюджетных и налоговых платежей. Дата документа (109)')),
                ('payer_status', models.CharField(blank=True, max_length=1000, verbose_name='Для бюджетных и налог. платежей. Статус плательщика(101)')),
                ('uin', models.CharField(blank=True, max_length=1000, verbose_name='Для бюджетных и налог. платежей. Уник. id начисления(22)')),
                ('sbp_oper_id', models.CharField(blank=True, max_length=1000, verbose_name='ID операций C2B платежа по СБП')),
                ('sbp_oper_id_for_refund', models.CharField(blank=True, max_length=1000, verbose_name='ID операции возврата С2B платежa')),
                ('rcv_qrc_id', models.CharField(blank=True, max_length=1000, verbose_name='ID QR-кода СБП')),
                ('account', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='accounts', to='modul_bank.account')),
            ],
            options={
                'verbose_name': 'Операция',
                'verbose_name_plural': 'Операции',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_id', models.CharField(max_length=1000, verbose_name='Уникальный id компании')),
                ('company_name', models.CharField(max_length=1000, verbose_name='Название компании')),
                ('status', models.BooleanField(verbose_name='Статус компании')),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companies', to='modul_bank.bank', verbose_name='Банк компании')),
            ],
            options={
                'verbose_name': 'Компания',
                'verbose_name_plural': 'Компании',
            },
        ),
        migrations.AddField(
            model_name='account',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to='modul_bank.company'),
        ),
    ]
