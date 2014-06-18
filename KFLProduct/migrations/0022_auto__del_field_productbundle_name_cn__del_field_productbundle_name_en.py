# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ProductBundle.name_cn'
        db.delete_column('KFLProduct_productbundle', 'name_cn')

        # Deleting field 'ProductBundle.name_en'
        db.delete_column('KFLProduct_productbundle', 'name_en')

        # Adding field 'ProductBundle.product_image'
        db.add_column('KFLProduct_productbundle', 'product_image',
                      self.gf('django.db.models.fields.files.ImageField')(blank=True, max_length=100, default=''),
                      keep_default=False)

        # Adding field 'ProductBundle.title_CN'
        db.add_column('KFLProduct_productbundle', 'title_CN',
                      self.gf('django.db.models.fields.CharField')(blank=True, max_length=30, null=True),
                      keep_default=False)

        # Adding field 'ProductBundle.title_EN'
        db.add_column('KFLProduct_productbundle', 'title_EN',
                      self.gf('django.db.models.fields.CharField')(blank=True, max_length=30, null=True),
                      keep_default=False)

        # Adding field 'ProductBundle.discription_CN'
        db.add_column('KFLProduct_productbundle', 'discription_CN',
                      self.gf('django.db.models.fields.TextField')(blank=True, max_length=10000, null=True),
                      keep_default=False)

        # Adding field 'ProductBundle.discription_EN'
        db.add_column('KFLProduct_productbundle', 'discription_EN',
                      self.gf('django.db.models.fields.TextField')(blank=True, max_length=10000, null=True),
                      keep_default=False)

        # Adding field 'ProductBundle.taobao_link'
        db.add_column('KFLProduct_productbundle', 'taobao_link',
                      self.gf('django.db.models.fields.URLField')(blank=True, max_length=200, null=True),
                      keep_default=False)

        # Adding field 'ProductBundle.paypal_button'
        db.add_column('KFLProduct_productbundle', 'paypal_button',
                      self.gf('django.db.models.fields.URLField')(blank=True, max_length=200, null=True),
                      keep_default=False)

        # Adding field 'ProductBundle.paypal_button_on_sale'
        db.add_column('KFLProduct_productbundle', 'paypal_button_on_sale',
                      self.gf('django.db.models.fields.URLField')(blank=True, max_length=200, null=True),
                      keep_default=False)

        # Adding M2M table for field language on 'ProductBundle'
        m2m_table_name = db.shorten_name('KFLProduct_productbundle_language')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('productbundle', models.ForeignKey(orm['KFLProduct.productbundle'], null=False)),
            ('language', models.ForeignKey(orm['KFLProduct.language'], null=False))
        ))
        db.create_unique(m2m_table_name, ['productbundle_id', 'language_id'])


    def backwards(self, orm):
        # Adding field 'ProductBundle.name_cn'
        db.add_column('KFLProduct_productbundle', 'name_cn',
                      self.gf('django.db.models.fields.CharField')(blank=True, max_length=30, null=True),
                      keep_default=False)

        # Adding field 'ProductBundle.name_en'
        db.add_column('KFLProduct_productbundle', 'name_en',
                      self.gf('django.db.models.fields.CharField')(blank=True, max_length=30, null=True),
                      keep_default=False)

        # Deleting field 'ProductBundle.product_image'
        db.delete_column('KFLProduct_productbundle', 'product_image')

        # Deleting field 'ProductBundle.title_CN'
        db.delete_column('KFLProduct_productbundle', 'title_CN')

        # Deleting field 'ProductBundle.title_EN'
        db.delete_column('KFLProduct_productbundle', 'title_EN')

        # Deleting field 'ProductBundle.discription_CN'
        db.delete_column('KFLProduct_productbundle', 'discription_CN')

        # Deleting field 'ProductBundle.discription_EN'
        db.delete_column('KFLProduct_productbundle', 'discription_EN')

        # Deleting field 'ProductBundle.taobao_link'
        db.delete_column('KFLProduct_productbundle', 'taobao_link')

        # Deleting field 'ProductBundle.paypal_button'
        db.delete_column('KFLProduct_productbundle', 'paypal_button')

        # Deleting field 'ProductBundle.paypal_button_on_sale'
        db.delete_column('KFLProduct_productbundle', 'paypal_button_on_sale')

        # Removing M2M table for field language on 'ProductBundle'
        db.delete_table(db.shorten_name('KFLProduct_productbundle_language'))


    models = {
        'KFLProduct.downloadproduct': {
            'Meta': {'object_name': 'downloadProduct'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'minute': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30', 'null': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'second': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'section_no': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'size': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'})
        },
        'KFLProduct.dvdproduct': {
            'DVD_quantity': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'Meta': {'object_name': 'DVDProduct'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['KFLProduct.ProductCategory']", 'null': 'True'}),
            'discription_CN': ('django.db.models.fields.TextField', [], {'blank': 'True', 'max_length': '10000', 'null': 'True'}),
            'discription_EN': ('django.db.models.fields.TextField', [], {'blank': 'True', 'max_length': '10000', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['KFLProduct.Language']", 'symmetrical': 'False', 'null': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'minute': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30', 'null': 'True'}),
            'online_download': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['KFLProduct.downloadProduct']", 'symmetrical': 'False', 'null': 'True'}),
            'paypal_button': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'paypal_button_on_sale': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'price_on_sale': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'product_image': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100'}),
            'second': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'taobao_link': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'title_CN': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30', 'null': 'True'}),
            'title_EN': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30', 'null': 'True'}),
            'youku_link': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'youtube_link': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'})
        },
        'KFLProduct.language': {
            'Meta': {'object_name': 'Language'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'pid': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'})
        },
        'KFLProduct.productbundle': {
            'Meta': {'object_name': 'ProductBundle'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['KFLProduct.ProductCategory']", 'symmetrical': 'False', 'null': 'True'}),
            'discription_CN': ('django.db.models.fields.TextField', [], {'blank': 'True', 'max_length': '10000', 'null': 'True'}),
            'discription_EN': ('django.db.models.fields.TextField', [], {'blank': 'True', 'max_length': '10000', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['KFLProduct.Language']", 'symmetrical': 'False', 'null': 'True'}),
            'paypal_button': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'paypal_button_on_sale': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'percent_off': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'product_image': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['KFLProduct.DVDProduct']", 'symmetrical': 'False', 'null': 'True'}),
            'taobao_link': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'title_CN': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30', 'null': 'True'}),
            'title_EN': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30', 'null': 'True'})
        },
        'KFLProduct.productcategory': {
            'Meta': {'object_name': 'ProductCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_cn': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30', 'null': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30', 'null': 'True'}),
            'pid': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'})
        },
        'KFLProduct.productcomment': {
            'Content': ('django.db.models.fields.TextField', [], {'blank': 'True', 'max_length': '10000', 'null': 'True'}),
            'Meta': {'object_name': 'ProductComment'},
            'following_comment': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['KFLProduct.ProductComment']", 'null': 'True'}),
            'following_product': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['KFLProduct.DVDProduct']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'posted_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['KFLProduct.UserProfile']", 'null': 'True'}),
            'posted_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'})
        },
        'KFLProduct.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'customer_number': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['KFLProduct.Language']"}),
            'last_viewed_product': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['KFLProduct.DVDProduct']", 'related_name': "'v_product'", 'symmetrical': 'False', 'null': 'True'}),
            'purchased_product': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['KFLProduct.DVDProduct']", 'related_name': "'p_product'", 'symmetrical': 'False', 'null': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Permission']", 'symmetrical': 'False'})
        },
        'auth.permission': {
            'Meta': {'object_name': 'Permission', 'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'blank': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Group']", 'related_name': "'user_set'", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['auth.Permission']", 'related_name': "'user_set'", 'symmetrical': 'False'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'object_name': 'ContentType', 'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)", 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['KFLProduct']