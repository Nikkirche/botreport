package com.example.botreport_android.util

import com.example.botreport_android.entities.LiveEvent
import com.example.botreport_android.entities.LiveNews
import dagger.Binds
import kotlinx.coroutines.Deferred
import retrofit2.Call
import retrofit2.Response
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import retrofit2.http.GET
import retrofit2.http.Path

private const val BASE_URL = "http://10.29.85.169:5000/api/"

private val retrofit = Retrofit.Builder()
    .addConverterFactory(GsonConverterFactory.create())
    .baseUrl(BASE_URL)
    .build()

interface BotReportApiService {
    @GET("live-news")
    fun getLiveEvents():Call<LiveNews>
}

object BotReportApi {
    val retrofitService: BotReportApiService by lazy {
        retrofit.create(BotReportApiService::class.java)
    }
}