def submit_request(request):
    form = SubmitRequest(request.POST or None)
    if form.is_valid():
        print form
        print dir(form)
        return HttpResponseRedirect('/thanks/') # Redirect after POST

    return render_to_response('contact.html', {
        'form': form,
    })