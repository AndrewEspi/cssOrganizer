# cssOrganizer - organize a css file by grouping them into categories
Developer: Andrew Espindola
Desciption: This python program was created to scan through a CSS file and produce a more organized CSS file by grouping related
            CSS Properties within selectors. Created in my spare time for fun and my own utility. It takes in a style.css file and
            creates a file called 'organized-style.css. I created this project to help me organize my css files and wanted to share it.
            There are a few rules and some drawbacks in this version, and this might be something I come back to update if I have some extra time.
            Feel free to tweek, update, and share with me if you feel it could be useful to you too!
            
When using the file
0) File to be organized should be 'style.css' and in the same directory level as cssOrganizer when run
1) Comments on the style.css can't be on a seperate line within the selectors, they can be on right of a property, accounting on separate lines could be future update
2) Curly braces must start on the same line as the css name, and end on a seperate line
3) Doesn't keep nested tabbed-in spacing (Such as media query spacing), could be a future update
4) Properties can be regrouped manually in the sortOrder list, easier customization could be future update

.example {
 background-color: teal; #Teal is my favorite color!
}


**Credit to csscomb.js on GitHub for the great list of all css properties!
