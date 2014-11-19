from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.core.files import File
from imagekit import ImageSpec
from imagekit.processors import ResizeToFill, Adjust

# class Thumbnail(ImageSpec):
#     processors = [ResizeToFill(100, 50)]
#     format = 'JPEG'
#     options = {'quality': 60}



# source_file = open('/path/to/myimage.jpg')
# image_generator = Thumbnail(source=source_file)
# result = image_generator.generate()


# dest = open('/path/to/dest.jpg', 'w')
# dest.write(result.read())
# dest.close()
import Image
class FilterImg(ImageSpec):
    processors = Adjust(contrast=1.2, sharpness=1.1,brightness =1.3),
    format = 'JPEG'
    options = {'quality': 100} 

#should pass a file
def changeBright(request):
    print "changeBright request"
    print "\n\n"
    # print "form: %s " % form
    print "the value of request.POST: %s" % request.POST
    print "the value of request.FILES: %s" % request.FILES

    #print "before assigning form: %s" % UploadFileForm(request.POST, request.FILES)
    # m = Image.open(infile)
    # im.save(outfile, "JPEG")
    #if request.method == 'POST':
    source_file = open('geo7a.jpg')
    print "source_file :%s" % source_file
    image_generator = FilterImg(source=source_file)
    result = image_generator.generate()
    dest = file('test.jpg', 'w')
    dest.write(result.read())
    dest.close()
    return
    # return render_to_response('dropzone-drag-drop.html', context_instance=RequestContext(request))

