# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table('KFLProduct_userprofile')

        # Removing M2M table for field last_viewed_product on 'UserProfile'
        db.delete_table(db.shorten_name('KFLProduct_userprofile_last_viewed_product'))

        # Removing M2M table for field purchased_product on 'UserProfile'
        db.delete_table(db.shorten_name('KFLProduct_userprofile_purchased_product'))


    def backwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table('KFLProduct_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['auth.User'])),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['KFLProduct.Language'])),
            ('customer_number', self.gf('django.db.models.fields.CharField')(null=True, max_length=30, blank=True)),
        ))
        db.send_create_signal('KFLProduct', ['UserProfile'])

        # Adding M2M table for field last_viewed_product on 'UserProfile'
        m2m_table_name = db.shorten_name('KFLProduct_userprofile_last_viewed_product')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm['KFLProduct.userprofile'], null=False)),
            ('dvdproduct', models.ForeignKey(orm['KFLProduct.dvdproduct'], null=False))
        ))
        db.create_unique(m2m_table_name, ['userprofile_id', 'dvdproduct_id'])

        # Adding M2M table for field purchased_product on 'UserProfile'
        m2m_table_name = db.shorten_name('KFLProduct_userprofile_purchased_product')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm['KFLProduct.userprofile'], null=False)),
            ('dvdproduct', models.ForeignKey(orm['KFLProduct.dvdproduct'], null=False))
        ))
        db.create_unique(m2m_table_name, ['userprofile_id', 'dvdproduct_id'])


    models = {
        'KFLProduct.downloadproduct': {
            'Meta': {'object_name': 'downloadProduct'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'}),
            'minute': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '30', 'blank': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'second': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'section_no': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'KFLProduct.dvdproduct': {
            'DVD_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'DVDProduct'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['KFLProduct.ProductCategory']"}),
            'discription_CN': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '10000', 'blank': 'True'}),
            'discription_EN': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '10000', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'blank': 'True', 'to': "orm['KFLProduct.Language']"}),
            'level': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'minute': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '30', 'blank': 'True'}),
            'online_download': ('django.db.models.fields.related.ManyToManyField', [], {'null': 'True', 'blank': 'True', 'to': "orm['KFLProduct.downloadProduct']", 'symmetrical': 'False'}),
            'paypal_button': ('django.db.models.fields.URLField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'second': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'taobao_link': ('django.db.models.fields.URLField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'}),
            'title_CN': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '30', 'blank': 'True'}),
            'title_EN': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '30', 'blank': 'True'}),
            'youku_link': ('django.db.models.fields.URLField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'}),
            'youtube_link': ('django.db.models.fields.URLField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'})
        },
        'KFLProduct.language': {
            'Meta': {'object_name': 'Language'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'KFLProduct.productcategory': {
            'Meta': {'object_name': 'ProductCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '30', 'blank': 'True'})
        }
    }

    complete_apps = ['KFLProduct']