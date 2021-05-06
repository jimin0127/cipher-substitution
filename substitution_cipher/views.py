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
        if request.POST['input_key'] == '':
            return render(
                request,
                'substitution_cipher/index.html',
                {

                }
            )

        if request.POST['ad'] == 'simple':
            key = request.POST['input_key']
            text = request.POST['input_plaintext']

            s = simple(key, text)
            cryptogram, key_list, alpha_list = s.process()
            alpha_key_list = zip(alpha_list, key_list)
            decryption = s.process2(cryptogram)

            if 'cryptogram_btn' in request.POST:

                return render(
                    request,
                    'substitution_cipher/index.html',
                    {
                        'key':key,
                        'text':text,
                        'type': 1,
                        'cryptogram' : cryptogram,
                        'alpha_key_list' : alpha_key_list,
                        'alpha_list':alpha_list,
                        'key_list':key_list
                    }
                )
            if 'decryption_btn' in request.POST :
                return render(
                    request,
                    'substitution_cipher/index.html',
                    {
                        'key': key,
                        'text': text,
                        'type': 1,
                        'cryptogram': cryptogram,
                        'decryption': decryption,
                        'alpha_key_list': alpha_key_list,
                        'alpha_list': alpha_list,
                        'key_list': key_list
                    }
                )

        elif request.POST['ad'] == 'multi':
            key = request.POST['input_key']
            text = request.POST['input_plaintext']

            s = multi(key, text)
            key_list, word_list = s.process()
            cryptogram = s.pro(word_list, key_list)
            decryption = s.decryption(cryptogram, key_list)
            request.POST['ad']

            if 'cryptogram_btn' in request.POST:
                return render(
                    request,
                    'substitution_cipher/index.html',
                    {
                        'key':key,
                        'text':text,
                        'type':2,
                        'cryptogram': cryptogram,
                        'key_list':key_list,
                        'word_list':word_list
                    }
                )
            if 'decryption_btn' in request.POST:
                return render(
                    request,
                    'substitution_cipher/index.html',
                    {
                        'key': key,
                        'text': text,
                        'type': 2,
                        'cryptogram': cryptogram,
                        'decryption': decryption,
                        'key_list': key_list,
                        'word_list': word_list
                    }
                )


def decryption(request):
    return None