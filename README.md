# Wideo
Convert a Wikipedia page to Video

# Quick run 
Download the HTML file, opne and clikc "Play" to see the Short Video Sample generated for wiki page "Elinor Ostrom".

# Python Script

The python script is used to generate json file containing images and text content , which are required for slideshow and audio synthesis.

Required package : wikipedia
pip/conda install wikipedia

# Try on your own
Once the JSON file is generated (presently only for 10 lines, you can change this to generate for entire wiki page) :
- Upload the JSON file to a server (like http://myjson.com/)
- Use the generated link in the Veiwer.HTML file (search for the old link and replace)
- Open Viewer.html and click play to see the output

# Improvements
- Crowdsource : A viewer must be able to flag an image, so that we replace the non-sensical ones.
