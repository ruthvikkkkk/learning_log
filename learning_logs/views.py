from django.shortcuts import render
from .models import Topic, Entry

from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import TopicForm, EntryForm

# Create your views here.
def index(request):
	"""The home page for our website."""
	return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
	"""Shows all the topics."""
	topics = Topic.objects.filter(owner = request.user).order_by('date_added')
	context = {'topics': topics}
	return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
	"""Shows the entries of a topic."""
	topic = Topic.objects.get(id = topic_id)
	if topic.owner != request.user:
		raise Http404

	entries = topic.entry_set.order_by('-date_added') #minus sign sorts in reverse order
	context = {'topic': topic, 'entries': entries}
	return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
	"""A form to add a new topic."""
	if request.method != 'POST':
		# If there is no data to sumit, create a blank form
		form = TopicForm()
	else:
		# If the data is submitted, process the data.
		form = TopicForm(request.POST)
		if form.is_valid():
			new_topic = form.save(commit = False)
			new_topic.owner = request.user
			new_topic.save()
			return HttpResponseRedirect(reverse('learning_logs:topics'))

	context = {'form': form}
	return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
	"""To add a new entry for a topic"""
	topic = Topic.objects.get(id = topic_id)

	if request.method != 'POST':
		# Blank Form
		form = EntryForm()
	else:
		# Data submitted, process data
		form = EntryForm(data = request.POST)
		if form.is_valid():
			new_entry = form.save(commit = False)
			new_entry.topic = topic
			new_entry.save()
			return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))

	context = {'topic': topic, 'form': form}
	return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
	"""Edit an existing entry."""
	entry = Entry.objects.get(id = entry_id)
	topic = entry.topic
	if topic.owner != request.user:
		raise Http404

	if request.method != 'POST':
		# Pre fill the form with existing data
		form = EntryForm(instance = entry)

	else:
		# process data
		form = EntryForm(instance = entry, data = request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:topic', args = [topic.id]))
	
	context = {'entry': entry, 'topic': topic, 'form': form}
	return render(request, 'learning_logs/edit_entry.html', context)