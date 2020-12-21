package com.example.botreport_android.util

import io.ktor.client.HttpClient
import io.ktor.client.engine.cio.CIO
import io.ktor.client.features.json.JsonFeature
import io.ktor.client.features.json.serializer.KotlinxSerializer
import io.ktor.util.KtorExperimentalAPI
import kotlinx.serialization.json.Json
import kotlinx.serialization.json.nonstrict
import javax.inject.Singleton
class NetworkStuff {
    @KtorExperimentalAPI
    val okHttpKtor = HttpClient(CIO) {
        install(JsonFeature) {
            serializer = KotlinxSerializer(Json.Default)
        }
    }
}