from evernote.api.client import EvernoteClient
import evernote.edam.type.ttypes as Types

dev_token = "S=s1:U=679e3:E=150952a1f8e:C=1493d78f2a8:P=1cd:A=en-devtoken:V=2:H=af92536299f84db9870ea3e3701f2ce3"
client = EvernoteClient(token=dev_token)
#userStore = client.get_user_store()
#user = userStore.getUser()
#print user.username

noteStore = client.get_note_store()
#notebooks = noteStore.listNotebooks()
#for n in notebooks:
#	print n.name

#note = Types.Note()
#note.title = "Test note"
#note.content = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
#note.content += '<en-note>note content</en-note>'
#note = noteStore.createNote(note)

noteStore = client.get_note_store()
notebook = Types.Notebook()
notebook.name = "My Notebook"
notebook = noteStore.createNotebook(notebook)
print notebook.guid