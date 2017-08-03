#!/bin/bash

import json
import datetime

with open("peoplebyinitials-formatted.json") as f:
    data = json.load(f)
 
    print("initials;initials-all;full-name;first-name;last-name;action-object;description;date-of-birth")
 
    for character in data:
        other = character["Persondata"]

        description = ""
        date_of_birth = ""

        metadata = {}
        for field in other.split("|"):
            if "=" not in field:  # <!-- Metadata: see [[Wikipedia:Persondata]]. -->\n
                continue 
            parts = field.split("=")
            value = parts[1].strip()
            if value:
                metadata[parts[0].strip()] = value

        if "SHORT DESCRIPTION" in metadata:
            description = metadata["SHORT DESCRIPTION"]
        if "DATE OF BIRTH" in metadata:
            date_of_birth = metadata["DATE OF BIRTH"]
            date_of_birth_obj = None
            try:
                date_of_birth_obj = datetime.datetime.strptime(date_of_birth, "%B %d, %Y")
            except Exception:
                try:
                    date_of_birth_obj = datetime.datetime.strptime(date_of_birth, "%d %B %Y")
                except Exception:
                    try:
                        date_of_birth_obj = datetime.datetime.strptime(date_of_birth, "%Y-%m-%d")
                    except Exception:
                        try:
                            date_of_birth_obj = datetime.datetime.strptime(date_of_birth, "%Y")
                        except Exception:
                            pass

            if date_of_birth_obj:
                date_of_birth = date_of_birth_obj.strftime("%Y-%m-%d")       
            else:
                date_of_birth = ""
 
        print("%s;%s;%s;%s;%s;%s;%s;%s" % (character["Initials_two"], character["Initials_all"], character["Page_title"], character["First_name"], character["Last_name"], "", description, date_of_birth))
