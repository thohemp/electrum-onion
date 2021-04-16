from pythonforandroid.recipe import CythonRecipe


class X13HashRecipe(CythonRecipe):

    url = ('https://files.pythonhosted.org/packages/78/d1/dfd9b0f2b095787ce6da6876199e71681773cfab22321e63174e05919b6c/deeponion-x13-hash-{version}.tar.gz')
    md5sum = '08c55917bc73a3552d332c1bd11e0b0a'
    version = '1.0.4'
    depends = ['python3', 'setuptools']
    call_hostpython_via_targetpython = False


recipe = X13HashRecipe()
