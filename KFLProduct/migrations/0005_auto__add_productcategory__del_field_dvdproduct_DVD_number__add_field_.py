# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProductCategory'
        db.create_table('KFLProduct_productcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
        ))
        db.send_create_signal('KFLProduct', ['ProductCategory'])

        # Deleting field 'DVDProduct.DVD_number'
        db.delete_column('KFLProduct_dvdproduct', 'DVD_number')

        # Adding field 'DVDProduct.category'
        db.add_column('KFLProduct_dvdproduct', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['KFLProduct.ProductCategory'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'DVDProduct.DVD_quantity'
        db.add_column('KFLProduct_dvdproduct', 'DVD_quantity',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'ProductCategory'
        db.delete_table('KFLProduct_productcategory')

        # Adding field 'DVDProduct.DVD_number'
        db.add_column('KFLProduct_dvdproduct', 'DVD_number',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'DVDProduct.category'
        db.delete_column('KFLProduct_dvdproduct', 'category_id')

        # Deleting field 'DVDProduct.DVD_quantity'
        db.delete_column('KFLProduct_dvdproduct', 'DVD_quantity')


    models = {
        'KFLProduct.downloadproduct': {
            'Meta': {'object_name': 'downloadProduct'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'minute': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'second': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'section_no': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'KFLProduct.dvdproduct': {
            'DVD_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'DVDProduct'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['KFLProduct.ProductCategory']", 'null': 'True', 'blank': 'True'}),
            'discription_CN': ('django.db.models.fields.CharField', [], {'max_length': '10000', 'null': 'True', 'blank': 'True'}),
            'discription_EN': ('django.db.models.fields.CharField', [], {'max_length': '10000', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'minute': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'online_download': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['KFLProduct.downloadProduct']", 'null': 'True', 'blank': 'True', 'symmetrical': 'False'}),
            'paypal_button': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'second': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'taobao_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'title_CN': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'title_EN': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'youku_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'youtube_link': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'KFLProduct.productcategory': {
            'Meta': {'object_name': 'ProductCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['KFLProduct']