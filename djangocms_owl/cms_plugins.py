# -*- coding: utf-8 -*-
from cms.models import CMSPlugin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool


class OwlPlugin(CMSPluginBase):
	name = u'Carousel'
	model = OwlPluginModel
	render_template = "djangocms_owl/"
	allow_children = True
	cache = True

	def render(self, context, instance, placeholder):
		context.update({'instance':instance})
		return context

plugin_pool.register_plugin(OwlPlugin)
