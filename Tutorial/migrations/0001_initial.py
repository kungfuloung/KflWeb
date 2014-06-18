# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'VideoTutorial'
        db.create_table('Tutorial_videotutorial', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('topic_CN', self.gf('django.db.models.fields.CharField')(blank=True, max_length=50, null=True)),
            ('topic_EN', self.gf('django.db.models.fields.CharField')(blank=True, max_length=50, null=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, null=True, to=orm['Tutorial.TutorialCategory'])),
            ('season', self.gf('django.db.models.fields.IntegerField')(blank=True, null=True)),
            ('episode', self.gf('django.db.models.fields.IntegerField')(blank=True, null=True)),
            ('youtube_link', self.gf('django.db.models.fields.URLField')(blank=True, max_length=200, null=True)),
            ('youku_link', self.gf('django.db.models.fields.URLField')(blank=True, max_length=200, null=True)),
        ))
        db.send_create_signal('Tutorial', ['VideoTutorial'])

        # Adding model 'TutorialCategory'
        db.create_table('Tutorial_tutorialcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(blank=True, max_length=30, null=True)),
        ))
        db.send_create_signal('Tutorial', ['TutorialCategory'])


    def backwards(self, orm):
        # Deleting model 'VideoTutorial'
        db.delete_table('Tutorial_videotutorial')

        # Deleting model 'TutorialCategory'
        db.delete_table('Tutorial_tutorialcategory')


    models = {
        'Tutorial.tutorialcategory': {
            'Meta': {'object_name': 'TutorialCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '30', 'null': 'True'})
        },
        'Tutorial.videotutorial': {
            'Meta': {'object_name': 'VideoTutorial'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['Tutorial.TutorialCategory']"}),
            'episode': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'season': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'topic_CN': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '50', 'null': 'True'}),
            'topic_EN': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '50', 'null': 'True'}),
            'youku_link': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'}),
            'youtube_link': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200', 'null': 'True'})
        }
    }

    complete_apps = ['Tutorial']