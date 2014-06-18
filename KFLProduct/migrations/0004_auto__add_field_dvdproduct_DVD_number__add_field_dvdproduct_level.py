# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'DVDProduct.DVD_number'
        db.add_column('KFLProduct_dvdproduct', 'DVD_number',
                      self.gf('django.db.models.fields.IntegerField')(blank=True, null=True),
                      keep_default=False)

        # Adding field 'DVDProduct.level'
        db.add_column('KFLProduct_dvdproduct', 'level',
                      self.gf('django.db.models.fields.IntegerField')(blank=True, null=True),
                      keep_default=False)

        # Adding M2M table for field online_download on 'DVDProduct'
        m2m_table_name = db.shorten_name('KFLProduct_dvdproduct_online_download')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('dvdproduct', models.ForeignKey(orm['KFLProduct.dvdproduct'], null=False)),
            ('downloadproduct', models.ForeignKey(orm['KFLProduct.downloadproduct'], null=False))
        ))
        db.create_unique(m2m_table_name, ['dvdproduct_id', 'downloadproduct_id'])


    def backwards(self, orm):
        # Deleting field 'DVDProduct.DVD_number'
        db.delete_column('KFLProduct_dvdproduct', 'DVD_number')

        # Deleting field 'DVDProduct.level'
        db.delete_column('KFLProduct_dvdproduct', 'level')

        # Removing M2M table for field online_download on 'DVDProduct'
        db.delete_table(db.shorten_name('KFLProduct_dvdproduct_online_download'))


    models = {
        'KFLProduct.downloadproduct': {
            'Meta': {'object_name': 'downloadProduct'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'minute': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '30'}),
            'price': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'second': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'section_no': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'size': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'})
        },
        'KFLProduct.dvdproduct': {
            'DVD_number': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'Meta': {'object_name': 'DVDProduct'},
            'discription_CN': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '10000'}),
            'discription_EN': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '10000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'minute': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '30'}),
            'online_download': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['KFLProduct.downloadProduct']"}),
            'paypal_button': ('django.db.models.fields.URLField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'price': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'second': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'taobao_link': ('django.db.models.fields.URLField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'title_CN': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '30'}),
            'title_EN': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '30'}),
            'youku_link': ('django.db.models.fields.URLField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'}),
            'youtube_link': ('django.db.models.fields.URLField', [], {'blank': 'True', 'null': 'True', 'max_length': '200'})
        }
    }

    complete_apps = ['KFLProduct']