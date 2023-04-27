from django.http import JsonResponse


def remove_letter(request):
    if request.method == 'GET':
        original_string = request.GET.get('string')
        letter_to_remove = request.GET.get('letter')
        if original_string and letter_to_remove:
            if len(letter_to_remove) > 1:
                return JsonResponse("Enter a single letter.", safe=False)
            letter_to_remove_upper = letter_to_remove.upper()
            letter_to_remove_lower = letter_to_remove.lower()
            updated_string = original_string.replace(letter_to_remove_upper, '')
            updated_string = updated_string.replace(letter_to_remove_lower, '')

            return JsonResponse(updated_string, safe=False)
        return JsonResponse("A string or a letter is missing from request.", safe=False)

