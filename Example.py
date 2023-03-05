from LibraCodex import *

"""_Note_
  1.don't forgot including r on front your user_path When put in these function even paths being a absolute path or not.
  (if you're feel unsure in some situation.)
  - add_paths
  - add_paths_by_absolute
  - update_paths
  
  2. in preview function will showing all exist path  on LibraCodex's dictionary container.
   -this method about show and didn't return an values anything.
   
  3. if want just choose to work use these function.
  -select_to_codex  =  chosen paths from you're desire to get.
  -full_to_codex = get all multiple paths in once times.
  
  4. in configure_path must be exist tag from your list on main base's container.
  
    """

#inheritance a LibraCodex into being an base's container by dictionary.
C = LibraCodex()

#add you're paths by including always tag_name and r in user_path.
C.add_paths(tag_name,user_path)

#add paths only absolute paths.
C.add_paths_by_absolute(tag_name, users_paths)

#update more paths and must including r in user_path.
C.update_paths(tag_name, new_user_path)

#show a data paths from main base's container.
C.preview()

#get paths from you're desire to working with.
path_by = C.path_chooser(tag_name)
print(path_by)

#set a default path by reference on exist tag name.
C.configure_path(reference_tags_1, reference_tags_2)

#clear all paths 
C.washing_paths()

#get // paths into \ 
Result_path = paths_converter(old_path)
print(Result)