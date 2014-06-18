# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table('KFLProduct_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['auth.User'])),
            ('customer_number', self.gf('django.db.models.fields.CharField')(blank=True, max_length=30, null=True)),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['KFLProduct.Language'])),
        ))
        db.send_create_signal('KFLProduct', ['UserProfile'])

        # Adding M2M table for field purchased_product on 'UserProfile'
        m2m_table_name = db.shorten_name('KFLProduct_userprofile_purchased_product')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm['KFLProduct.userprofile'], null=False)),
            ('dvdproduct', models.ForeignKey(orm['KFLProduct.dvdproduct'], null=False))
        ))
        db.create_unique(m2m_table_name, ['userprofile_id', 'dvdproduct_id'])

        # Adding M2M table for field last_viewed_product on 'UserProfile'
        m2m_table_name = db.shorten_name('KFLProduct_userprofile_last_viewed_product')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm['KFLProduct.userprofile'], null=False)),
            ('dvdproduct', models.ForeignKey(orm['KFLProduct.dvdproduct'], null=False))
        ))
        db.create_unique(m2m_table_name, ['userprofile_id', 'dvdproduct_id'])


    def backwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table('KFLProduct_userprofile')

        # Removing M2M table for field purchased_product on 'UserProfile'
        db.delete_table(db.shorten_name('KFLProduct_userprofile_purchased_product'))

        # Removing M2M table for field last_viewed_product on 'UserProfile'
        db.delete_table(db.shorten_name('KFLProduct_userprofile_last_viewed_product'))


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
            'discription_CN': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '10000', 'null': 'True'}),
            'discription_EN': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '10000', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'to': "orm['KFLProduct.Language']", 'null': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'minute': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30', 'null': 'True'}),
            'online_download': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'to': "orm['KFLProduct.downloadProduct']", 'null': 'True', 'symmetrical': 'False'}),
            'paypal_button': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'KFLProduct.productcategory': {
            'Meta': {'object_name': 'ProductCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30', 'null': 'True'})
        },
        'KFLProduct.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'customer_number': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['KFLProduct.Language']"}),
            'last_viewed_product': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'v_product'", 'blank': 'True', 'to': "orm['KFLProduct.DVDProduct']", 'null': 'True', 'symmetrical': 'False'}),
            'purchased_product': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'p_product'", 'blank': 'True', 'to': "orm['KFLProduct.DVDProduct']", 'null': 'True', 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'unique': 'True', 'to': "orm['auth.User']"})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'blank': 'True', 'to': "orm['auth.Group']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'blank': 'True', 'to': "orm['auth.Permission']", 'symmetrical': 'False'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'object_name': 'ContentType', 'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'", 'ordering': "('name',)"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['KFLProduct']