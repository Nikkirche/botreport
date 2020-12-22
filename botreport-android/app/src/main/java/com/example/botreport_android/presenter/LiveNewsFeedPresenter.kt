package com.example.botreport_android.presenter

import androidx.lifecycle.MutableLiveData
import com.example.botreport_android.entities.LiveEvent
import com.example.botreport_android.models.LiveNewsFeedModel
import com.example.botreport_android.views.LiveNewsFeedView
import moxy.MvpPresenter
import javax.inject.Inject

class LiveNewsFeedPresenter @Inject constructor(model: LiveNewsFeedModel) :MvpPresenter<LiveNewsFeedView>() {
    val newsList = MutableLiveData<LiveEvent>()

    @Inject
    lateinit var model: LiveNewsFeedModel
    fun firstlyLoadNews() {
        //model.getData()
        //viewState.setInAdapter(model.eventsData)

    }
}