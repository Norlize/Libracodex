from LibraCodex import *

"""_Note_
  1.don't forgot including r on front your user_path When put in these function.
  -add_paths(tag_name,user_path)
  -update_paths(tag_name,user_path)
  
  2. in preview function will showing all exist path  on LibraCodex's dictionary container.
   -this method about show and didn't return anything.
   
  3. if want just choose to work use these function.
  -select_to_codex  =  chosen paths from you're desire to get.
  -full_to_codex = get all multiple paths in once times.
  
    """



#inheritance base's container
C = LibraCodex()

#add you're paths by including always tag_name and r in user_path
C.add_paths(tag_name,user_path)

#update more paths and must including r in user_path
C.update_paths(tag_name, new_user_path)

#show a data paths from main base's container
C.preview()

#get paths from you're desire to working with.
C.select_to_codex(tag_name)

#return all paths in once time.
C.full_to_codex()

#clear all paths 
C.washing_paths()

