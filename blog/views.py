from django.shortcuts import render

from models import Article
from home.views import BaseView

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class HomeView(BaseView):
	def get_context_data(self, page=1, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)
		articles = Article.objects.filter(published=True).order_by('-date_published').all()
		
		context["featured_article"] = articles[0]
		context["last_news"] = articles[1:4]

		page_articles = []
		paginator = Paginator(articles, 3)

		try:
			page_articles = paginator.page(page)
		except PageNotAnInteger:
			page = 1
			page_articles = paginator.page(page)
		except EmptyPage:
			page = paginator.num_pages
			page_articles = paginator.page(page)

		context["page_articles"] = page_articles
		context["page_number"] = page
		context["page_total_number"] = paginator.num_pages

		return context

	def get(self, request, page=1):
		return render(request, 'news.html', self.get_context_data(page=page))

class ArticleView(BaseView):
	def get_context_data(self, article_id=None, article_slug=None, **kwargs):
		context = super(ArticleView, self).get_context_data(**kwargs)
		if article_id:
			context['article'] = Article.objects.get(id=article_id)
		else:
			context['article'] = Article.objects.get(slug=article_slug)

		return context

	def get(self, request, article_id=None, article_slug=None):
		return render(request, 'article.html', self.get_context_data(article_id=article_id, article_slug=article_slug))
