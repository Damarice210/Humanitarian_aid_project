# # from django.shortcuts import render

# # # Create your views here.

# # from django.shortcuts import render
# # from .models import AidItem, DistributionCenter, AidDistribution
# # from django.http import JsonResponse

# # def home(request):
# #     aid_items = AidItem.objects.all()
# #     distribution_centers = DistributionCenter.objects.all()
# #     return render(request, 'relief/home.html', {'aid_items': aid_items, 'distribution_centers': distribution_centers})


# # def distribute_aid(request):
# #     if request.method == 'POST':
# #         aid_item_id = request.POST.get('aid_item')
# #         distribution_center_id = request.POST.get('distribution_center')
# #         quantity = int(request.POST.get('quantity'))
        
# #         aid_item = AidItem.objects.get(id=aid_item_id)
# #         distribution_center = DistributionCenter.objects.get(id=distribution_center_id)
        
# #         # Check if this distribution has already occurred for the day
# #         if AidDistribution.objects.filter(aid_item=aid_item, distribution_center=distribution_center, date_of_distribution__date=request.POST.get('date')).exists():
# #             return JsonResponse({'message': 'This distribution has already been logged for today.'}, status=400)
        
# #         # Create new distribution record
# #         distribution = AidDistribution(
# #             aid_item=aid_item,
# #             # distribution_center=distribution_center,
# #             quantity_distributed=quantity,
# #             date_of_distribution=request.POST.get('date')
# #         )
# #         distribution.save()
        
# #         return JsonResponse({'message': 'Aid distributed successfully!'}, status=200)

# from django.shortcuts import render
# from .models import AidItem, DistributionCenter, AidDistribution
# from django.http import JsonResponse

# def home(request):
#     aid_items = AidItem.objects.all()
#     distribution_centers = DistributionCenter.objects.all()
#     return render(request, 'relief/home.html', {'aid_items': aid_items, 'distribution_centers': distribution_centers})


# def distribute_aid(request):
#     if request.method == 'POST':
#         aid_item_id = request.POST.get('aid_item')
#         distribution_center_id = request.POST.get('distribution_center')
#         quantity = int(request.POST.get('quantity'))
        
#         aid_item = AidItem.objects.get(id=aid_item_id)
#         distribution_center = DistributionCenter.objects.get(id=distribution_center_id)
        
#         # Check if this distribution has already occurred for the day
#         if AidDistribution.objects.filter(aid_item=aid_item, distribution_center=distribution_center, date_of_distribution__date=request.POST.get('date')).exists():
#             return JsonResponse({'message': 'This distribution has already been logged for today.'}, status=400)
        
#         # Create new distribution record
#         distribution = AidDistribution(
#             aid_item=aid_item,
#             distribution_center=distribution_center,
#             # quantity_distributed=quantity,
#             date_of_distribution=request.POST.get('date')
#         )
#         distribution.save()
        
#         return JsonResponse({'message': 'Aid distributed successfully!'}, status=200)

from django.shortcuts import render
from django.http import JsonResponse

from .models import AidItem, DistributionCenter

def home(request):
    aid_items = AidItem.objects.all()
    distribution_centers = DistributionCenter.objects.all()
    return render(request, 'relief/home.html', {
        'aid_items': aid_items,
        'distribution_centers': distribution_centers,
    })

def distribute_aid(request):
    if request.method == 'POST':
        # Example logic for distribution
        return JsonResponse({'message': 'Aid distributed successfully!'})
    return JsonResponse({'message': 'Invalid request'})
