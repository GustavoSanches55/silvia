# Generated by Django 4.1.3 on 2022-11-06 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_aluno', models.CharField(max_length=50)),
                ('genero_aluno', models.CharField(blank=True, max_length=20, null=True)),
                ('data_nascimento_aluno', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='assunto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_assunto', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carga_horaria', models.IntegerField()),
                ('id_assunto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.assunto')),
            ],
        ),
        migrations.CreateModel(
            name='instituicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_instituicao', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='sentimentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_sentimentos', models.CharField(max_length=50)),
                ('carater', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.CharField(max_length=50)),
                ('periodo', models.IntegerField()),
                ('tag', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=50)),
                ('senha', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_professor', models.CharField(max_length=50)),
                ('genero_professor', models.CharField(blank=True, max_length=20, null=True)),
                ('data_nascimento_professor', models.DateField()),
                ('id_insituicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.instituicao')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='instituicao',
            name='id_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.usuario'),
        ),
        migrations.CreateModel(
            name='grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.aluno')),
                ('id_disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.disciplina')),
            ],
        ),
        migrations.AddField(
            model_name='disciplina',
            name='id_professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.professor'),
        ),
        migrations.AddField(
            model_name='disciplina',
            name='id_turma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.turma'),
        ),
        migrations.CreateModel(
            name='avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.CharField(blank=True, max_length=500, null=True)),
                ('conhecimento', models.IntegerField()),
                ('intensidade', models.IntegerField()),
                ('data', models.DateField()),
                ('id_aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.aluno')),
                ('id_disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.disciplina')),
                ('id_sentimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.sentimentos')),
            ],
        ),
        migrations.AddField(
            model_name='aluno',
            name='id_insituicao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.instituicao'),
        ),
        migrations.AddField(
            model_name='aluno',
            name='id_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.usuario'),
        ),
    ]
