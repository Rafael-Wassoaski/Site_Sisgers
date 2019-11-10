# Generated by Django 2.2.7 on 2019-11-10 00:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vistoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cobrad', models.CharField(max_length=200)),
                ('municipios', models.TextField()),
                ('descricao', models.TextField()),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
                ('endereco', models.TextField()),
                ('dataDesastre', models.TextField()),
                ('danos_humanos_desalojados', models.IntegerField(blank=True, default=0)),
                ('danos_humanos_desabrigados', models.IntegerField(blank=True, default=0)),
                ('danos_humanos_desaparecidos', models.IntegerField(blank=True, default=0)),
                ('danos_humanos_feridos', models.IntegerField(blank=True, default=0)),
                ('danos_humanos_enfermos', models.IntegerField(blank=True, default=0)),
                ('danos_humanos_mortos', models.IntegerField(blank=True, default=0)),
                ('danos_humanos_isolados', models.IntegerField(blank=True, default=0)),
                ('danos_humanos_atingidos', models.IntegerField(blank=True, default=0)),
                ('danos_humanos_afetados', models.IntegerField(blank=True, default=0)),
                ('danos_humanos_observacoes', models.TextField(blank=True, default='Sem Observações')),
                ('unidades_habitacionais_atingidas', models.IntegerField(blank=True, default=0)),
                ('unidades_habitacionais_danificads', models.IntegerField(blank=True, default=0)),
                ('unidades_habitacionais_interditadas', models.IntegerField(blank=True, default=0)),
                ('unidades_habitacionais_destruidas', models.IntegerField(blank=True, default=0)),
                ('instalacoes_publicas_saude_atingidas', models.IntegerField(blank=True, default=0)),
                ('instalacoes_publicas_ensino_atingidas', models.IntegerField(blank=True, default=0)),
                ('instalacoes_comunitarias_atingidas', models.IntegerField(blank=True, default=0)),
                ('obras_atingidas', models.IntegerField(blank=True, default=0)),
                ('interrupcoes_servicos_essenciais', models.IntegerField(blank=True, default=0)),
                ('danos_materiais_observacoes', models.TextField(blank=True, default='Sem Observações')),
                ('contaminacao_solo', models.IntegerField(blank=True, default=0)),
                ('contaminacao_agua', models.IntegerField(blank=True, default=0)),
                ('contaminacao_ar', models.IntegerField(blank=True, default=0)),
                ('danos_ambientais_observacoes', models.TextField(blank=True, default='Sem Observações')),
                ('danos_agricultura', models.IntegerField(blank=True, default=0)),
                ('danos_pecuaria', models.IntegerField(blank=True, default=0)),
                ('danos_industria', models.IntegerField(blank=True, default=0)),
                ('danos_comercio', models.IntegerField(blank=True, default=0)),
                ('danos_prestacao_de_servicos', models.IntegerField(blank=True, default=0)),
                ('danos_economicos_observacoes', models.TextField(blank=True, default='Sem Observações')),
                ('iah_cestas_de_alimentos', models.IntegerField(blank=True, default=0)),
                ('iah_agua_potavel', models.IntegerField(blank=True, default=0)),
                ('iah_colchoes', models.IntegerField(blank=True, default=0)),
                ('iah_kit_higiene_pessoal', models.IntegerField(blank=True, default=0)),
                ('iah_kit_limpeza', models.IntegerField(blank=True, default=0)),
                ('iah_telhas', models.IntegerField(blank=True, default=0)),
                ('iah_lona_plastica', models.IntegerField(blank=True, default=0)),
                ('iah_outros', models.IntegerField(blank=True, default=0)),
                ('iah_fornecidos_outros_observacoes', models.TextField(blank=True, default='Sem Observações')),
                ('iah_vias_publicas_totalmente_desobistruidas', models.BooleanField(default=False)),
                ('iah_reestabelecimento_servicos_essenciais', models.BooleanField(default=False)),
                ('deferido', models.BooleanField(blank=True, default=False)),
                ('latitude', models.CharField(max_length=20)),
                ('longitude', models.CharField(max_length=20)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autor_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
