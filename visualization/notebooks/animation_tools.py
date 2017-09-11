"""
This animation_tools module contains tools to create animations in Python and
Jupyter notebooks.

Two types of animations are supported: 
 - using the ipywidget interact to create a figure with a slider bar, 
 - using JSAnimation to create Javascript code that loops over a set of 
   images and adds controls to play as an animation.

The set of images to combine in an animation can be specified as a
list of images, a list of `matplotlib` figures, or a directory of
`png` or other image files.

Utilities are provided to convert between these.

See also:
 https://ipywidgets.readthedocs.io/en/latest/#ipywidgets
 https://github.com/jakevdp/JSAnimation

More documentation of these functions is needed and they can probably be
improved.

Work in progress by R. J. LeVeque, feel free to adapt them to your needs.
The CC-BY License is used for this and all Geohackweek materials:
   https://geohackweek.github.io/visualization/license/

These tools will eventually be incorporated into VisClaw,
   https://github.com/clawpack/visclaw

"""

# use Python 3 style print function rather than Python 2 print statements:
from __future__ import print_function 

from IPython.display import display
from matplotlib import image, animation
from matplotlib import pyplot as plt
from ipywidgets import interact, interact_manual
import ipywidgets
import io
from matplotlib import pyplot as plt

try:
    from JSAnimation import IPython_display
    found_JSAnim = True
except:
    try:
        from clawpack.visclaw.JSAnimation import IPython_display
        found_JSAnim = True
    except:
        found_JSAnim = False


def make_plotdir(plotdir='_plots', clobber=True):
    """
    Utility function to create a directory for storing a sequence of plot
    files, or if the directory already exists, clear out any old plots.  
    If clobber==False then it will abort instead of deleting existing files.
    """

    import os
    if os.path.isdir(plotdir):
        if clobber:
            os.system("rm %s/*" % plotdir)
        else:
            raise IOError('*** Cannot clobber existing directory %s' % plotdir)
    else:
        os.system("mkdir %s" % plotdir)
    print("Figure files for each frame will be stored in ", plotdir)


def save_frame(frameno, plotdir='_plots', fname_base='frame', format='png',
               verbose=False, **kwargs):
    """
    After giving matplotlib commands to create the plot for a single frame 
    of the desired animation, this can be called to save the figure with
    the appropriate file name such as _plots/frame00001.png.
    """

    plt.draw()
    filename = '%s/%s%s.%s' % (plotdir, fname_base, str(frameno).zfill(5), format)
    plt.savefig(filename, **kwargs)
    if verbose:
        print("Saved ",filename)


def make_anim(plotdir, fname_pattern='frame*.png', figsize=(10,6), dpi=None):
    """
    Assumes that a set of frames are available as png files in directory _plots,
    numbered consecutively, e.g. frame0000.png, frame0001.png, etc.

    Creates an animation based display each frame in turn, and returns anim.

    You can then display anim in an IPython notebook, or
    call make_html(anim) to create a stand-alone webpage.
    """

    import glob   # for finding all files matching a pattern

    if not found_JSAnim:
        raise ImportError('*** JSAnimation package not found')

    # Find all frame files:
    filenames = glob.glob('%s/%s' % (plotdir, fname_pattern))

    # sort them into increasing order:
    filenames=sorted(filenames)

    fig = plt.figure(figsize=figsize, dpi=dpi)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')  # so there's not a second set of axes
    im = plt.imshow(image.imread(filenames[0]))

    def init():
        im.set_data(image.imread(filenames[0]))
        return im,

    def animate(i):
        image_i=image.imread(filenames[i])
        im.set_data(image_i)
        return im,

    anim = animation.FuncAnimation(fig, animate, init_func=init,
                          frames=len(filenames), interval=200, blit=True)

    return anim


def JSAnimate_images(images, figsize=(10,6), dpi=None):

    fig = plt.figure(figsize=figsize, dpi=None)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')  # so there's not a second set of axes

    im = plt.imshow(images[0])

    def init():
        im.set_data(images[0])
        return im,

    def animate(i):
        im.set_data(images[i])
        return im,

    anim = animation.FuncAnimation(fig, animate, init_func=init,
                          frames=len(images), interval=200, blit=True)

    return anim


def make_html(anim, file_name='anim.html', title=None, raw_html='', \
              fps=None, embed_frames=True, default_mode='once'):
    """
    Take an animation created by make_anim and convert it into a stand-alone
    html file.
    """

    if not found_JSAnim:
        raise ImportError('*** JSAnimation package not found')

    from JSAnimation.IPython_display import anim_to_html


    html_body = anim_to_html(anim, fps=fps, embed_frames=embed_frames, \
                 default_mode=default_mode)

    html_file = open(file_name,'w')
    html_file.write("<html>\n <h1>%s</h1>\n" % title)
    html_file.write(raw_html)
    html_file.write(html_body)
    html_file.close()
    print("Created %s" % file_name)


def read_images(plotdir, fname_pattern='*.png'):

    import glob, os
    images = []
    files = glob.glob(os.path.join(plotdir, fname_pattern))
    for file in files:
        im = plt.imread(file)
        images.append(im)
    return images

def save_images(images, figsize=(8,6), plotdir='_plots', clobber=True, \
                fname_base='frame', format='png', verbose=False, **kwargs):

    make_plotdir(plotdir=plotdir, clobber=clobber)
    for frameno,image in enumerate(images):
        fig = imshow_noaxes(image, figsize)
        filename = '%s/%s%s.%s' % (plotdir, fname_base, str(frameno).zfill(5), format)
        plt.savefig(filename, format=format, **kwargs)
        plt.close(fig)
        if verbose:
            print("Saved ",filename)

def save_figs(figs, plotdir='_plots', clobber=True, \
                fname_base='frame', format='png', verbose=False, **kwargs):

    make_plotdir(plotdir=plotdir, clobber=clobber)
    for frameno,fig in enumerate(figs):
        filename = '%s/%s%s.%s' % (plotdir, fname_base, str(frameno).zfill(5), format)
        fig.savefig(filename, format=format, **kwargs)
        plt.close(fig)
        if verbose:
            print("Saved ",filename)


def make_image(fig, **kwargs):
    """
    Take a matplotlib figure *fig* and convert it to an image *im* that 
    can be viewed with imshow.
    """

    import io
    png = io.BytesIO()
    fig.savefig(png,format='png', **kwargs)
    png.seek(0)
    im = plt.imread(png)
    return im

def make_images(figs, **kwargs):
    """
    Take a list of matplotlib figures *figs* and convert to list of images.
    """

    images = []
    for fig in figs:
        im = make_image(fig, **kwargs)
        images.append(im)
    return images

def imshow_noaxes(im, figsize=(8,6)):
    fig = plt.figure(figsize=figsize)
    ax = plt.axes()
    plt.imshow(im)
    ax.axis('off')
    return fig
    
def interact_animate_images(images, figsize=(10,6), manual=False, TextInput=False):

    def display_frame(frameno): 
        imshow_noaxes(images[frameno], figsize=figsize)

    if TextInput:
        if TextInput:
            print("Valid frameno values: from %i to %i" % (0,len(images)-1))
        widget = ipywidgets.IntText(min=0,max=len(images)-1, value=0)
    else:
        widget = ipywidgets.IntSlider(min=0,max=len(images)-1, value=0)

    if manual:
        interact_manual(display_frame, frameno=widget)
    else:
        interact(display_frame, frameno=widget)

def interact_animate_figs(figs, manual=False, TextInput=False):

    def display_frame(frameno): 
        display(figs[frameno])

    if TextInput:
        widget = ipywidgets.IntText(min=0,max=len(figs)-1, value=0)
    else:
        widget = ipywidgets.IntSlider(min=0,max=len(figs)-1, value=0)

    if manual:
        if TextInput:
            print("Valid frameno values: from %i to %i" % (0,len(figs)-1))
        interact_manual(display_frame, frameno=widget)
    else:
        interact(display_frame, frameno=widget)

