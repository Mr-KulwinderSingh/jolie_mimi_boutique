from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile, NewsletterSubscription
from .forms import UserProfileForm, ChangePasswordForm
from checkout.models import Order

from .forms import UserProfileForm, ChangePasswordForm


@login_required
def profile(request):
    user = request.user
    profile = get_object_or_404(UserProfile, user=user)
    orders = profile.orders.all().order_by('-date')

    # user_profile_form = UserProfileForm(instance=request.user.userprofile)
    # password_form = ChangePasswordForm(user=request.user)  # ✅ pass user here

    # Initialize context
    context = {
        'orders': orders,
        'profile': profile,
        'on_profile_page': True
    }

    # Initialize user profile, password and newsletter forms
    user_profile_form = UserProfileForm(instance=profile)
    password_form = ChangePasswordForm(user)
    # newsletter_form = ProfileNewsletterUpdate(instance=profile)

    # Checking request userprofileform/changepassword form/newsletter checkbox
    if request.method == 'POST':
        if 'user_username' in request.POST:
            # Handle UserProfileForm
            user_profile_form = UserProfileForm(
                request.POST, request.FILES, instance=profile)
            # User/Profile info form
            if user_profile_form.is_valid():
                profile = user_profile_form.save(commit=False)
                profile.user.username = user_profile_form.cleaned_data[
                    'user_username']
                profile.user.email = user_profile_form.cleaned_data[
                    'user_email']
                profile.user.first_name = user_profile_form.cleaned_data[
                    'user_first_name']
                profile.user.last_name = user_profile_form.cleaned_data[
                    'user_last_name']
                profile.user.save()

                # Save the newsletter subscription status
                # subscribe_newsletter = request.POST.get('subscribe_newsletter')
                # Convert to boolean
                # profile.subscribe_newsletter = bool(subscribe_newsletter)
                # profile.save()

                # Handle newsletter subscription
                # if subscribe_newsletter:
                #     Create or update the NewsletterSubscription object
                #     subscription, created = (
                #         NewsletterSubscription.objects
                #         .get_or_create(user_profile=profile)
                #     )
                #     Set the email address
                #     subscription.email = profile.user.email
                #     subscription.save()
                # else:
                #     Delete NewsletterSubscription object associated with user
                #     NewsletterSubscription.objects.filter(
                #         user_profile=profile).delete()
                #     newsletter_form.initial['subscribe_newsletter'] = False

                profile.save()
                messages.success(request, 'Profile updated successfully')
            else:
                messages.error(
                    request, 'Please ensure the profile information is valid.')
        elif 'old_password' in request.POST:
            password_form = ChangePasswordForm(user, request.POST)
            if password_form.is_valid():
                user = password_form.save()
                messages.success(request, 'Password changed successfully')
            else:
                messages.error(
                    request, 'Please correct the password change form errors.')
    else:
        user_profile_form = UserProfileForm(instance=profile)
        password_form = ChangePasswordForm(user)
        # newsletter_form = ProfileNewsletterUpdate(instance=profile)

    # Set initial value for newsletter subscription checkbox
    # if NewsletterSubscription.objects.filter(email=user.email).exists():
    #     newsletter_form.initial['subscribe_newsletter'] = True

    context['user_profile_form'] = user_profile_form
    context['password_form'] = password_form
    # context['newsletter_form'] = newsletter_form

    template = 'profiles/profile.html'
    return render(request, template, context)


@login_required
def change_password(request):
    user = request.user

    if request.method == 'POST':
        # Handle ChangePasswordForm
        password_form = ChangePasswordForm(user, request.POST)
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password changed successfully')
        else:
            messages.error(
                request, 'Password change failed. Please correct the errors.')

    return redirect(reverse('profile'))


@login_required
def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    # Check if the current user is the owner of the order
    if order.user_profile.user != request.user:
        # If not, return a 403 Forbidden response
        return HttpResponseForbidden(render(request, 'errors/403.html'))

    template = 'profiles/order_detail.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


# @login_required
# def profile(request):
#     """ Display the user's profile. """
#     profile = get_object_or_404(UserProfile, user=request.user)

#     if request.method == 'POST':
#         form = UserProfileForm(request.POST, instance=profile)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Profile updated successfully')
#         else:
#             messages.error(request, 'Update failed. Ensure the form is valid.')
#     else:
#         form = UserProfileForm(instance=profile)
#     orders = profile.orders.all()

#     template = 'profiles/profile.html'
#     context = {
#         'form': form,
#         'orders': orders,
#         'on_profile_page': True
#     }

#     return render(request, template, context)


# def order_history(request, order_number):
#     order = get_object_or_404(Order, order_number=order_number)

#     messages.info(request, (
#         f'This is a past confirmation for order number {order_number}. '
#         'A confirmation email was sent on the order date.'
#     ))

#     template = 'checkout/checkout_success.html'
#     context = {
#         'order': order,
#         'from_profile': True,
#     }

#     return render(request, template, context)
