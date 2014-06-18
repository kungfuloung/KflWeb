# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'TutorialCategory.discription_CN'
        db.add_column('Tutorial_tutorialcategory', 'discription_CN',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True, max_length=10000),
                      keep_default=False)

        # Adding field 'TutorialCategory.discription_EN'
        db.add_column('Tutorial_tutorialcategory', 'discription_EN',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True, max_length=10000),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'TutorialCategory.discription_CN'
        db.delete_column('Tutorial_tutorialcategory', 'discription_CN')

        # Deleting field 'TutorialCategory.discription_EN'
        db.delete_column('Tutorial_tutorialcategory', 'discription_EN')


    models = {
        'KFLProduct.downloadproduct': {
            'Meta': {'object_name': 'downloadProduct'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'minute': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '30'}),
            'price': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'second': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'section_no': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'size': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'KFLProduct.dvdproduct': {
            'DVD_quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'DVDProduct'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['KFLProduct.ProductCategory']", 'blank': 'True'}),
            'discription_CN': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True', 'max_length': '10000'}),
            'discription_EN': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True', 'max_length': '10000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ManyToManyField', [], {'null': 'True', 'to': "orm['KFLProduct.Language']", 'symmetrical': 'False', 'blank': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'minute': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '30'}),
            'online_download': ('django.db.models.fields.related.ManyToManyField', [], {'null': 'True', 'to': "orm['KFLProduct.downloadProduct']", 'symmetrical': 'False', 'blank': 'True'}),
            'paypal_button': ('django.db.models.fields.URLField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'paypal_button_on_sale': ('django.db.models.fields.URLField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'price': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'price_on_sale': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'product_image': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100'}),
            'second': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'taobao_link': ('django.db.models.fields.URLField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'title_CN': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '30'}),
            'title_EN': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '30'}),
            'youku_link': ('django.db.models.fields.URLField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'youtube_link': ('django.db.models.fields.URLField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'})
        },
        'KFLProduct.language': {
            'Meta': {'object_name': 'Language'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'pid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'KFLProduct.productcategory': {
            'Meta': {'object_name': 'ProductCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_cn': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '30'}),
            'name_en': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '30'}),
            'pid': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'KFLProduct.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'customer_number': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['KFLProduct.Language']"}),
            'last_viewed_product': ('django.db.models.fields.related.ManyToManyField', [], {'null': 'True', 'to': "orm['KFLProduct.DVDProduct']", 'symmetrical': 'False', 'blank': 'True', 'related_name': "'v_product'"}),
            'purchased_product': ('django.db.models.fields.related.ManyToManyField', [], {'null': 'True', 'to': "orm['KFLProduct.DVDProduct']", 'symmetrical': 'False', 'blank': 'True', 'related_name': "'p_product'"}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'Tutorial.tutorialcategory': {
            'Meta': {'object_name': 'TutorialCategory'},
            'discription_CN': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True', 'max_length': '10000'}),
            'discription_EN': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True', 'max_length': '10000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '30'}),
            'title_CN': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '30'}),
            'title_EN': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '30'}),
            'tutorial_pic': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100'})
        },
        'Tutorial.tutorialcomment': {
            'Content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True', 'max_length': '10000'}),
            'Meta': {'object_name': 'TutorialComment'},
            'following_comment': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['Tutorial.TutorialComment']", 'blank': 'True'}),
            'following_tutorial': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['Tutorial.VideoTutorial']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'posted_by': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['KFLProduct.UserProfile']", 'blank': 'True'}),
            'posted_on': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        'Tutorial.videotutorial': {
            'Meta': {'object_name': 'VideoTutorial'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['Tutorial.TutorialCategory']", 'blank': 'True'}),
            'episode': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minute': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'season': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'second': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'topic_CN': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '50'}),
            'topic_EN': ('django.db.models.fields.CharField', [], {'null': 'True', 'blank': 'True', 'max_length': '50'}),
            'youku_link': ('django.db.models.fields.URLField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'}),
            'youtube_link': ('django.db.models.fields.URLField', [], {'null': 'True', 'blank': 'True', 'max_length': '200'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True', 'related_name': "'user_set'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True', 'related_name': "'user_set'"}),
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

    complete_apps = ['Tutorial']