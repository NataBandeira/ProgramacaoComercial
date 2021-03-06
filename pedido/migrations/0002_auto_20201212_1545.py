# Generated by Django 3.1.3 on 2020-12-12 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0001_initial'),
        ('homepage', '0001_initial'),
        ('pedido', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='endereco',
        ),
        migrations.AddField(
            model_name='pedido',
            name='endereco_entrega',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.endereco'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='quantidade',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='itempedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loja.produto'),
        ),
        migrations.DeleteModel(
            name='ItemPedido',
        ),
    ]
