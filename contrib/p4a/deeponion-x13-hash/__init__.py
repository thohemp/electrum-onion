from pythonforandroid.recipe import CythonRecipe


class X13HashRecipe(CythonRecipe):

    url = ('https://files.pythonhosted.org/packages/'
           'source/x/deeponion-x13-hash/deeponion-x13-hash-{version}.tar.gz')
    md5sum = '08c55917bc73a3552d332c1bd11e0b0a'
    version = '1.0.4'
    depends = ['python3']


recipe = X13HashRecipe()
