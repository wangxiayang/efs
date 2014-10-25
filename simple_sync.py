#!/usr/bin/python

from evernote.api.client import EvernoteClient
import evernote.edam.type.ttypes as Types
from evernote.edam.notestore import NoteStore

dev_token = "S=s1:U=679e3:E=150952a1f8e:C=1493d78f2a8:P=1cd:A=en-devtoken:V=2:H=af92536299f84db9870ea3e3701f2ce3"
client = EvernoteClient(token=dev_token)

noteStore = client.get_note_store()

# notebooks = noteStore.listNotebooks()
# for notebook in notebooks:
# 	print notebook.name, notebook.guid

# tags = noteStore.listTags()
# for tag in tags:
# 	print tag.name, tag.guid

# sync from Notebook to client
filter = NoteStore.NoteFilter()
# filter.words = "tag:sync_paper"
filter.notebookGuid = "fc3768d2-db91-48dc-ad10-55099350aa1f"
filter.tagGuids = ['570fdfbe-0a06-425c-aa26-49ddd2ba2991']

spec = NoteStore.NotesMetadataResultSpec()
spec.includeTitle = True
spec.includeUpdated = True
notelist = noteStore.findNotesMetadata(dev_token, filter, 0, 65535, spec)
for note in notelist.notes:
	noteEntity = noteStore.getNote(dev_token, note.guid, True, False, False, False)
	import datetime
	# print 'title', note.title, datetime.datetime.fromtimestamp(int(note.updated)).strftime('%Y-%m-%d %H:%M:%S')
	print 'title', note.title
	# print datatime.fromtimestamp(note.updated)
	# for resource in noteEntity.resources:
	# 	print resource.attributes.fileName
	# 	print 'try to get pdf file'
	# 	pdfresource = noteStore.getResourceData(dev_token, resource.guid)
	# 	file = open(resource.attributes.fileName, 'w')
	# 	print 'try to write into file'
	# 	file.write(pdfresource)
	# 	print 'success'
	# 	file.close()