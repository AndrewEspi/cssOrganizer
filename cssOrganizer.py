#Developer: Andrew Espindola
#Desciption: This python program was created to scan through a CSS file and produce a more organized CSS file by grouping related
#            CSS Properties within selectors. Created in my spare time for fun and my own utility. I probably won't get to updating this too much.
#
#0) File to be organized should be 'style.css' and in the same directory level as cssOrganizer when run
#1) Comments on the style.css can't be on a seperate line within the selectors, they can be on right of a property, accounting on separate lines could be future update
#2) Curly braces must start on the same line as the css name, and end on a seperate line
#3) Doesn't keep nested tabbed-in spacing (Such as media query spacing), could be a future update
#4) Properties can be regrouped manually in the property list, easier customization could be future update
#
# .example {
#   background-color: teal; #Teal is my favorite color!
# }
#

def reOrganizeCSSFile(lines):

    #This list of categories attributed to csscomb.js project on GitHub, thanks for the comprehensive list!
    #Can be reorganized for preference
    sortOrder = [
        #Font category
        [
            "font",
            "font-family",
            "font-size",
            "font-weight",
            "font-style",
            "font-variant",
            "font-size-adjust",
            "font-stretch",
            "font-effect",
            "font-emphasize",
            "font-emphasize-position",
            "font-emphasize-style",
            "font-smooth",
            "line-height"
        ],
        #Position category
        [
            "position",
            "z-index",
            "top",
            "right",
            "bottom",
            "left"
        ],
        #Flex, Display, align, grid, etc category
        [
            "display",
            "visibility",
            "float",
            "clear",
            "overflow",
            "overflow-x",
            "overflow-y",
            "-ms-overflow-x",
            "-ms-overflow-y",
            "clip",
            "zoom",
            "-webkit-align-content",
            "-ms-flex-line-pack",
            "grid-template-columns",
            "grid-template-rows",
            "grid-template-areas",
            "grid-area",
            "gap",
            "align-content",
            "-webkit-box-align",
            "-moz-box-align",
            "-webkit-align-items",
            "align-items",
            "-ms-flex-align",
            "-webkit-align-self",
            "-ms-flex-item-align",
            "-ms-grid-row-align",
            "align-self",
            "-webkit-box-flex",
            "-webkit-flex",
            "-moz-box-flex",
            "-ms-flex",
            "flex",
            "-webkit-flex-flow",
            "-ms-flex-flow",
            "flex-flow",
            "-webkit-flex-basis",
            "-ms-flex-preferred-size",
            "flex-basis",
            "-webkit-box-orient",
            "-webkit-box-direction",
            "-webkit-flex-direction",
            "-moz-box-orient",
            "-moz-box-direction",
            "-ms-flex-direction",
            "flex-direction",
            "-webkit-flex-grow",
            "-ms-flex-positive",
            "flex-grow",
            "-webkit-flex-shrink",
            "-ms-flex-negative",
            "flex-shrink",
            "-webkit-flex-wrap",
            "-ms-flex-wrap",
            "flex-wrap",
            "-webkit-box-pack",
            "-moz-box-pack",
            "-ms-flex-pack",
            "-webkit-justify-content",
            "justify-content",
            "-webkit-box-ordinal-group",
            "-webkit-order",
            "-moz-box-ordinal-group",
            "-ms-flex-order",
            "order"
        ],
        #Margin, Padding, and size category
        [
            "-webkit-box-sizing",
            "-moz-box-sizing",
            "box-sizing",
            "width",
            "min-width",
            "max-width",
            "height",
            "min-height",
            "max-height",
            "margin",
            "margin-top",
            "margin-right",
            "margin-bottom",
            "margin-left",
            "padding",
            "padding-top",
            "padding-right",
            "padding-bottom",
            "padding-left"
        ],
        #List category
        [
            "table-layout",
            "empty-cells",
            "caption-side",
            "border-spacing",
            "border-collapse",
            "list-style",
            "list-style-position",
            "list-style-type",
            "list-style-image"
        ],
        #Animation and some text category
        [
            "content",
            "quotes",
            "counter-reset",
            "counter-increment",
            "resize",
            "cursor",
            "-webkit-user-select",
            "-moz-user-select",
            "-ms-user-select",
            "user-select",
            "nav-index",
            "nav-up",
            "nav-right",
            "nav-down",
            "nav-left",
            "-webkit-transition",
            "-moz-transition",
            "-ms-transition",
            "-o-transition",
            "transition",
            "-webkit-transition-delay",
            "-moz-transition-delay",
            "-ms-transition-delay",
            "-o-transition-delay",
            "transition-delay",
            "-webkit-transition-timing-function",
            "-moz-transition-timing-function",
            "-ms-transition-timing-function",
            "-o-transition-timing-function",
            "transition-timing-function",
            "-webkit-transition-duration",
            "-moz-transition-duration",
            "-ms-transition-duration",
            "-o-transition-duration",
            "transition-duration",
            "-webkit-transition-property",
            "-moz-transition-property",
            "-ms-transition-property",
            "-o-transition-property",
            "transition-property",
            "-webkit-transform",
            "-moz-transform",
            "-ms-transform",
            "-o-transform",
            "transform",
            "-webkit-transform-origin",
            "-moz-transform-origin",
            "-ms-transform-origin",
            "-o-transform-origin",
            "transform-origin",
            "-webkit-animation",
            "-moz-animation",
            "-ms-animation",
            "-o-animation",
            "animation",
            "-webkit-animation-name",
            "-moz-animation-name",
            "-ms-animation-name",
            "-o-animation-name",
            "animation-name",
            "-webkit-animation-duration",
            "-moz-animation-duration",
            "-ms-animation-duration",
            "-o-animation-duration",
            "animation-duration",
            "-webkit-animation-play-state",
            "-moz-animation-play-state",
            "-ms-animation-play-state",
            "-o-animation-play-state",
            "animation-play-state",
            "-webkit-animation-timing-function",
            "-moz-animation-timing-function",
            "-ms-animation-timing-function",
            "-o-animation-timing-function",
            "animation-timing-function",
            "-webkit-animation-delay",
            "-moz-animation-delay",
            "-ms-animation-delay",
            "-o-animation-delay",
            "animation-delay",
            "-webkit-animation-iteration-count",
            "-moz-animation-iteration-count",
            "-ms-animation-iteration-count",
            "-o-animation-iteration-count",
            "animation-iteration-count",
            "-webkit-animation-direction",
            "-moz-animation-direction",
            "-ms-animation-direction",
            "-o-animation-direction",
            "animation-direction",
            "text-align",
            "-webkit-text-align-last",
            "-moz-text-align-last",
            "-ms-text-align-last",
            "text-align-last",
            "vertical-align",
            "white-space",
            "text-decoration",
            "text-emphasis",
            "text-emphasis-color",
            "text-emphasis-style",
            "text-emphasis-position",
            "text-indent",
            "-ms-text-justify",
            "text-justify",
            "letter-spacing",
            "word-spacing",
            "-ms-writing-mode",
            "text-outline",
            "text-transform",
            "text-wrap",
            "text-overflow",
            "-ms-text-overflow",
            "text-overflow-ellipsis",
            "text-overflow-mode",
            "-ms-word-wrap",
            "word-wrap",
            "word-break",
            "-ms-word-break",
            "-moz-tab-size",
            "-o-tab-size",
            "tab-size",
            "-webkit-hyphens",
            "-moz-hyphens",
            "hyphens",
            "pointer-events"
        ],
        #Border, background, and shadow category
        [
            "opacity",
            "filter:progid:DXImageTransform.Microsoft.Alpha(Opacity",
            "-ms-filter:\\'progid:DXImageTransform.Microsoft.Alpha",
            "-ms-interpolation-mode",
            "color",
            "border",
            "border-width",
            "border-style",
            "border-color",
            "border-top",
            "border-top-width",
            "border-top-style",
            "border-top-color",
            "border-right",
            "border-right-width",
            "border-right-style",
            "border-right-color",
            "border-bottom",
            "border-bottom-width",
            "border-bottom-style",
            "border-bottom-color",
            "border-left",
            "border-left-width",
            "border-left-style",
            "border-left-color",
            "-webkit-border-radius",
            "-moz-border-radius",
            "border-radius",
            "-webkit-border-top-left-radius",
            "-moz-border-radius-topleft",
            "border-top-left-radius",
            "-webkit-border-top-right-radius",
            "-moz-border-radius-topright",
            "border-top-right-radius",
            "-webkit-border-bottom-right-radius",
            "-moz-border-radius-bottomright",
            "border-bottom-right-radius",
            "-webkit-border-bottom-left-radius",
            "-moz-border-radius-bottomleft",
            "border-bottom-left-radius",
            "-webkit-border-image",
            "-moz-border-image",
            "-o-border-image",
            "border-image",
            "-webkit-border-image-source",
            "-moz-border-image-source",
            "-o-border-image-source",
            "border-image-source",
            "-webkit-border-image-slice",
            "-moz-border-image-slice",
            "-o-border-image-slice",
            "border-image-slice",
            "-webkit-border-image-width",
            "-moz-border-image-width",
            "-o-border-image-width",
            "border-image-width",
            "-webkit-border-image-outset",
            "-moz-border-image-outset",
            "-o-border-image-outset",
            "border-image-outset",
            "-webkit-border-image-repeat",
            "-moz-border-image-repeat",
            "-o-border-image-repeat",
            "border-image-repeat",
            "outline",
            "outline-width",
            "outline-style",
            "outline-color",
            "outline-offset",
            "background",
            "filter:progid:DXImageTransform.Microsoft.AlphaImageLoader",
            "filter",
            "background-color",
            "background-image",
            "background-repeat",
            "background-attachment",
            "background-position",
            "background-position-x",
            "-ms-background-position-x",
            "background-position-y",
            "-ms-background-position-y",
            "-webkit-background-clip",
            "-moz-background-clip",
            "background-clip",
            "background-origin",
            "-webkit-background-size",
            "-moz-background-size",
            "-o-background-size",
            "background-size",
            "object-fit",
            "box-decoration-break",
            "-webkit-box-shadow",
            "-moz-box-shadow",
            "box-shadow",
            "filter:progid:DXImageTransform.Microsoft.gradient",
            "-ms-filter:\\'progid:DXImageTransform.Microsoft.gradient",
            "text-shadow"
        ]
    ]

    file = open("organized-style.css", "w")

    tempLine = ""

    sortedLine = []

    placeMediaBracket = False

    #Go through the lines, stop before the last line (It would be a } anyway)
    for i in range(0, len(lines)-1):

        #Get rid of extra space
        tempLine = lines[i].strip()

        #Check if its a blank line
        if len(tempLine) > 0 and ('@' or '}') not in tempLine and '/*' not in tempLine[0:4]:

            #{ means it is the start of a new selector
            if '{' in tempLine:

                #Write the line to the file
                file.writelines(lines[i].strip()+"\n")

                #Pass in start of the selector (The next line after { found) to group every property by category
                sortedLine = categorizeSelectorLines(i+1, lines, sortOrder)

                #Reassemble the selector by newly category grouped CSS Properties
                for category in sortedLine:
                    for line in category:
                        if len(line) > 0:
                            if '}' in line:
                                file.writelines("}\n\n")
                            else:
                                #Put each of the sorted lines back into the file
                                file.writelines(line+"\n")

        elif len(tempLine) > 0:

            #Make sure that media changes get a final closing bracket before the start of the next media query
            if '@' in tempLine:
                
                if placeMediaBracket:

                    file.writelines("}" + "\n\n")

                placeMediaBracket = True
            
            file.writelines(lines[i].strip() + "\n")

    #Place another bracket to keep media query nesting
    if placeMediaBracket:
        file.writelines("}")

    file.close()

#Returns the CSS properties in a list, grouped by categories
#This can be refactored using a dictionary to reduce lookup time for repeated elements
def categorizeSelectorLines(i, lines, sortOrder):

    #A category list holding lists of the lines grouped by category + 1 extra for --var group
    categoryOrder = [[],[],[],[],[],[],[]]

    #Holds the grouped CSS Properties by catagory
    sortedLines = []

    #Scan lines till the end of the selector lines }, placing them in the 7+1 catagories
    while '}' not in lines[i]:
        
        #Only place the line in a category if a finished css line, otherwise combine CSS Properties that are on separate lines
        if ';' in lines[i]:

            cssPropertyName = lines[i].strip().split(":")[0]
            
            j = 0

            while cssPropertyName not in sortOrder[j] and j < len(sortOrder)-1:
                j +=1

            categoryOrder[j].append("    " + lines[i].strip())

        #When CSS property is seperated into multiple lines, combine the current line with the next one
        elif ':' in lines[i]:

            #If css property is on seperate lines, combine them and place them in the next spot for processing
            lines[i+1] = lines[i].strip() + " " + lines[i+1].strip()

        i += 1

    #Skip empty lists, ******************Later, added functionality can be implemented that sorts the categories based off the ordering within category***************
    for a in categoryOrder:
        if len(a) > 0:
            sortedLines.append(a)

    #Add the final } to close the line list
    sortedLines.append(lines[i].strip())

    #Return each of the lines in grouped order
    return sortedLines

#Main driver
if __name__ == "__main__":

    #Read in the style.css
    file = open("style.css", "r")

    lines = file.readlines()

    file.close()

    reOrganizeCSSFile(lines)
