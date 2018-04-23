# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-25 15:47

# Copyright (c) 2018 Josef Wachtler
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

'''
This is a database migration to add some initial data for the LTI consumer.
'''


from __future__ import unicode_literals

from django.db import migrations


def load_launch_params(apps, schema_editor):
    '''
    Saves all default launch parameters to its model.
    '''
    LP = apps.get_model('consumer', 'DefaultLaunchParam')
    LP.objects.create(name='lti_message_type', required=True)
    LP.objects.create(name='lti_version', required=True)
    LP.objects.create(name='resource_link_id', required=True)

    LP.objects.create(name='resource_link_description', required=False)
    LP.objects.create(name='resource_link_title', required=False)
    LP.objects.create(name='user_id', required=False)
    LP.objects.create(name='user_image', required=False)
    LP.objects.create(name='roles', required=False)
    LP.objects.create(name='lis_person_name_given', required=False)
    LP.objects.create(name='lis_person_name_family', required=False)
    LP.objects.create(name='lis_person_name_full', required=False)
    LP.objects.create(name='lis_person_contact_email_primary', required=False)
    LP.objects.create(name='role_scope_mentor', required=False)
    LP.objects.create(name='context_id', required=False)
    LP.objects.create(name='context_label', required=False)
    LP.objects.create(name='context_title', required=False)
    LP.objects.create(name='context_type', required=False)
    LP.objects.create(name='launch_presentation_locale', required=False)
    LP.objects.create(name='launch_presentation_document_target', required=False)
    LP.objects.create(name='launch_presentation_css_url', required=False)
    LP.objects.create(name='launch_presentation_width', required=False)
    LP.objects.create(name='launch_presentation_height', required=False)
    LP.objects.create(name='launch_presentation_return_url', required=False)
    LP.objects.create(name='tool_consumer_info_product_family_code', required=False)
    LP.objects.create(name='tool_consumer_info_version', required=False)
    LP.objects.create(name='tool_consumer_instance_guid', required=False)
    LP.objects.create(name='tool_consumer_instance_name', required=False)
    LP.objects.create(name='tool_consumer_instance_description', required=False)
    LP.objects.create(name='tool_consumer_instance_url', required=False)
    LP.objects.create(name='tool_consumer_instance_contact_email', required=False)
    LP.objects.create(name='lis_course_section_sourcedid', required=False)
    LP.objects.create(name='lis_course_offering_sourcedid', required=False)
    LP.objects.create(name='lis_outcome_service_url', required=False)
    LP.objects.create(name='lis_person_sourcedid', required=False)
    LP.objects.create(name='lis_result_sourcedid', required=False)
    LP.objects.create(name='lti_errormsg', required=False)
    LP.objects.create(name='lti_errorlog', required=False)
    LP.objects.create(name='lti_msg', required=False)
    LP.objects.create(name='lti_log', required=False)
    LP.objects.create(name='oauth_consumer_key', required=False)
    LP.objects.create(name='oauth_signature_method', required=False)
    LP.objects.create(name='oauth_timestamp', required=False)
    LP.objects.create(name='oauth_nonce', required=False)
    LP.objects.create(name='oauth_version', required=False)
    LP.objects.create(name='oauth_signature', required=False)
    LP.objects.create(name='oauth_callback', required=False)
    LP.objects.create(name='roles', required=False)
    LP.objects.create(name='role_scope_mentor', required=False)
    LP.objects.create(name='context_type', required=False)
    LP.objects.create(name='accept_media_types', required=False)
    LP.objects.create(name='accept_presentation_document_targets', required=False)
    LP.objects.create(name='selection_directive', required=False)
    LP.objects.create(name='text', required=False)


def unload_launch_params(apps, schema_editor):
    '''
    Deletes all default launch Parameters.
    '''
    LP = apps.get_model('consumer', 'DefaultLaunchParam')
    LP.objects.all().delete()


class Migration(migrations.Migration):
    '''
    Defines the careating and deleting of the default launch Parameters as
    a migration.
    '''

    dependencies = [
        ('consumer', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_launch_params,
                             reverse_code=unload_launch_params),
    ]
