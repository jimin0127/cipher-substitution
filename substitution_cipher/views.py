from django.shortcuts import render
from .simple_substitution import simple_substitution as simple
from .multiple_substitution import multiple_substitution as multi

# Create your views here.
def index(request):
    return render(
        request,
        'substitution_cipher/index.html',
        {}

    )

def substitution(request):
    if request.method == 'POST':
        if request.POST['ad'] == 'simple':
            key = request.POST['input_key']
            text = request.POST['input_plaintext']

            s = simple(key, text)
            cryptogram, key_list, alpha_list = s.process()
            alpha_key_list = zip(alpha_list, key_list)
            decryption = s.process2(cryptogram)
            return render(
                request,
                'substitution_cipher/simple.html',
                {
                    'cryptogram' : cryptogram,
                    'decryption' : decryption,
                    'alpha_key_list' : alpha_key_list,
                    'alpha_list':alpha_list,
                    'key_list':key_list
                }
            )
        elif request.POST['ad'] == 'multi':
            key = request.POST['input_key']
            text = request.POST['input_plaintext']

            s = multi(key, text)
            key_list, word_list = s.process()
            cryptogram = s.pro(word_list, key_list)
            return render(
                request,
                'substitution_cipher/multi.html',
                {
                    'cryptogram': cryptogram,
                    #'decryption': decryption.
                    'key_list':key_list,
                    'word_list':word_list
                }
            )

