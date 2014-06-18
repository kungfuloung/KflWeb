# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TutorialComment'
        db.create_table('Tutorial_tutorialcomment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('following_tutorial', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Tutorial.VideoTutorial'], blank=True, null=True)),
            ('following_comment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Tutorial.TutorialComment'], blank=True, null=True)),
            ('posted_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['KFLProduct.UserProfile'], blank=True, null=True)),
            ('posted_on', self.gf('django.db.models.fields.DateTimeField')(blank=True, null=True)),
            ('Content', self.gf('django.db.models.fields.TextField')(null=True, max_length=10000, blank=True)),
        ))
        db.send_create_signal('Tutorial', ['TutorialComment'])


    def backwards(self, orm):
        # Deleting model 'TutorialComment'
        db.delete_table('Tutorial_tutorialcomment')


    models = {
        'KFLProduct.downloadproduct': {
            'Meta': {'object_name': 'downloadProduct'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'}),
            'minute': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '30', 'blank': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'second': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'section_no': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'size': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'})
        },
        'KFLProduct.dvdproduct': {
            'DVD_quantity': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'Meta': {'object_name': 'DVDProduct'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['KFLProduct.ProductCategory']", 'blank': 'True', 'null': 'True'}),
            'discription_CN': ('django.db.models.fields.TextField', [], {'null': 'True', 'max_length': '10000', 'blank': 'True'}),
            'discription_EN': ('django.db.models.fields.TextField', [], {'null': 'True', 'max_length': '10000', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['KFLProduct.Language']", 'blank': 'True', 'null': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'minute': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '30', 'blank': 'True'}),
            'online_download': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['KFLProduct.downloadProduct']", 'blank': 'True', 'null': 'True'}),
            'paypal_button': ('django.db.models.fields.URLField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'}),
            'paypal_button_on_sale': ('django.db.models.fields.URLField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'price_on_sale': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'second': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
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
        },
        'KFLProduct.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'customer_number': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '30', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['KFLProduct.Language']"}),
            'last_viewed_product': ('django.db.models.fields.related.ManyToManyField', [], {'null': 'True', 'related_name': "'v_product'", 'to': "orm['KFLProduct.DVDProduct']", 'blank': 'True', 'symmetrical': 'False'}),
            'purchased_product': ('django.db.models.fields.related.ManyToManyField', [], {'null': 'True', 'related_name': "'p_product'", 'to': "orm['KFLProduct.DVDProduct']", 'blank': 'True', 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'Tutorial.tutorialcategory': {
            'Meta': {'object_name': 'TutorialCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '30', 'blank': 'True'})
        },
        'Tutorial.tutorialcomment': {
            'Content': ('django.db.models.fields.TextField', [], {'null': 'True', 'max_length': '10000', 'blank': 'True'}),
            'Meta': {'object_name': 'TutorialComment'},
            'following_comment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Tutorial.TutorialComment']", 'blank': 'True', 'null': 'True'}),
            'following_tutorial': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Tutorial.VideoTutorial']", 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'posted_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['KFLProduct.UserProfile']", 'blank': 'True', 'null': 'True'}),
            'posted_on': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'})
        },
        'Tutorial.videotutorial': {
            'Meta': {'object_name': 'VideoTutorial'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Tutorial.TutorialCategory']", 'blank': 'True', 'null': 'True'}),
            'episode': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'season': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'topic_CN': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '50', 'blank': 'True'}),
            'topic_EN': ('django.db.models.fields.CharField', [], {'null': 'True', 'max_length': '50', 'blank': 'True'}),
            'youku_link': ('django.db.models.fields.URLField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'}),
            'youtube_link': ('django.db.models.fields.URLField', [], {'null': 'True', 'max_length': '200', 'blank': 'True'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'to': "orm['auth.Group']", 'blank': 'True', 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'object_name': 'ContentType', 'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['Tutorial']