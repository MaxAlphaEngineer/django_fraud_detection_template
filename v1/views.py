# Create your views here.
from django.http import JsonResponse
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView


class ObtainTokenView(TokenObtainPairView):
    permission_classes = [AllowAny]


def submit(request):
    if request.method == 'GET':
        print(request.GET)
        sender = request.GET.get('sender')
        receiver = request.GET.get('receiver')

        if sender and receiver:
            # Perform the transaction creation logic using the sender and receiver values

            # ...

            # Return a success response

            return JsonResponse({'message': 'Transaction created successfully.'}, status=201)
        else:
            return JsonResponse({'error': 'Invalid sender or receiver value.'}, status=400)

        # Return an error for unsupported request methods or paths

    return JsonResponse({'error': 'Unsupported request.'}, status=405)
