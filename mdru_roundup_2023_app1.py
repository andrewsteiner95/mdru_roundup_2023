image = hv.RGB.load_image(r"C:\Users\asteiner\OneDrive - UBC\Documents\PostDoc\uXRF project\E947399_RGB.tif")
image.opts(xaxis=None,
           yaxis=None,
           data_aspect=1)

data = hv.RGB.load_image(r"C:\Users\asteiner\OneDrive - UBC\Documents\PostDoc\uXRF project\E947399_RGB_comb.png")
data.opts(xaxis=None, yaxis=None, data_aspect=1)

class Opacity(pm.Parameterized):
    Micro_XRF_Opacity = pm.Magnitude(default=1.0)

    def viewable(self, **kwargs):
        return data.apply.opts(alpha=self.param.Micro_XRF_Opacity)

lc = Opacity()
rock = pn.Column(
    pn.pane.Markdown('''
    ### ROCK 1
    '''),
                    image * lc.viewable(), lc.param, name = 'Rock 1')

questions = pn.pane.Markdown('''
#### Answer four correct for a chance to win a holiday to Mexico
## 1. What is the white mineral?
## 2. Do you like it?
## 3. Why not?
## 4. Why am I always hungry!?!?
## 5. Doctor, what's with this rash?

### <a href="https://docs.google.com/forms/d/e/1FAIpQLSdx3Vj67nYuO1D5rlGzxW84YcjTbEcncv3zmRn0k7Dd4jMmcw/viewform?vc=0&c=0&w=1&flr=0" target="_blank">Click here to submit answers</a>
 ''',
                             name='Questions')

image2 = hv.RGB.load_image(r"C:\Users\asteiner\OneDrive - UBC\Documents\PostDoc\uXRF project\Ken_Zn_image.png")
image2.opts(xaxis=None, yaxis=None, data_aspect=1)

data2 = hv.RGB.load_image(r"C:\Users\asteiner\OneDrive - UBC\Documents\PostDoc\uXRF project\Ken_Zn_data.png")
data2.opts(xaxis=None, yaxis=None, data_aspect=1)

class Opacity_(pm.Parameterized):
    Micro_XRF_Opacity = pm.Magnitude(default=1.0)

    def viewable_(self, **kwargs):
        return data2.apply.opts(alpha=self.param.Micro_XRF_Opacity)

lc2 = Opacity_()
rock2 = pn.Column(
    pn.pane.Markdown('''
    ### ROCK 2
    '''),
                    image2 * lc2.viewable_(), lc2.param, name = 'Rock 2')

pn.Tabs(questions, rock, rock2).servable()