from django.http import JsonResponse


def remove_letter(request):
    if request.method == 'GET':
        original_string = request.GET.get('string')
        letter_to_remove = request.GET.get('letter')
        if original_string and letter_to_remove:
            updated_string = original_string.replace(letter_to_remove, '')
            return JsonResponse(updated_string, safe=False)
        return JsonResponse("A string or a letter is missing from request.", safe=False)

