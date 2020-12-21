package com.example.botreport_android.models

import android.util.Log
import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.example.botreport_android.entities.LiveEvent
import com.example.botreport_android.entities.LiveNews
import com.example.botreport_android.util.BotReportApi
import com.example.botreport_android.util.BotReportApi.retrofitService
import com.example.botreport_android.util.BotReportApiService
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import java.util.Collections.addAll
import javax.inject.Inject
import javax.inject.Singleton

@Singleton
 class LiveNewsFeedModel @Inject constructor(){
    var eventsData: ArrayList<LiveEvent> = arrayListOf<LiveEvent>()

    fun getData() {
        val api = retrofitService.getLiveEvents()

        api.enqueue(object : Callback<LiveNews> {
            override fun onFailure(call: Call<LiveNews>, t: Throwable) {
                Log.e("network", call.request().url().toString())
                Log.e("network", t.toString())
            }
            override fun onResponse(call: Call<LiveNews>, response: Response<LiveNews>) {
                Log.e("network",response.body().toString())
                if(response.body() != null)
                    (response.body()!!.liveNews as ArrayList<LiveEvent>)
                    Log.e("solution&",eventsData.toString())

            }
        })
    }

}
