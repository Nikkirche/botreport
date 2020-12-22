package com.example.botreport_android.ui

import android.animation.Animator
import android.animation.AnimatorListenerAdapter
import android.content.Context
import android.os.Bundle
import android.util.Log
import android.util.TimeUtils
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ProgressBar
import android.widget.TextView
import androidx.fragment.app.FragmentManager
import androidx.fragment.app.add
import androidx.fragment.app.commit
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.example.botreport_android.R
import com.example.botreport_android.adapters.LiveNewsAdapter
import com.example.botreport_android.databinding.LiveNewsFeedFragmentBinding
import com.example.botreport_android.entities.LiveEvent
import com.example.botreport_android.entities.LiveNews
import com.example.botreport_android.presenter.LiveNewsFeedPresenter
import com.example.botreport_android.util.BotReportApi
import com.example.botreport_android.views.LiveNewsFeedView
import dagger.hilt.android.AndroidEntryPoint
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.MainScope
import kotlinx.coroutines.launch
import moxy.MvpAppCompatFragment
import moxy.ktx.moxyPresenter
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import java.sql.Time
import java.util.*
import javax.inject.Inject
import javax.inject.Provider
import kotlin.collections.ArrayList

@AndroidEntryPoint
class LiveNewsFeedFragment : MvpAppCompatFragment(), LiveNewsFeedView,
    CoroutineScope by MainScope() {
    @Inject
    lateinit var presenterProvider: Provider<LiveNewsFeedPresenter>
    private val presenter: LiveNewsFeedPresenter by moxyPresenter { presenterProvider.get() }
    lateinit var recyclerView: RecyclerView
    lateinit var recyclerAdapter: LiveNewsAdapter
    private var _binding: LiveNewsFeedFragmentBinding? = null
    private val binding get() = _binding!!
    private var shortAnimationDuration: Int = 0
    lateinit var progressBar: ProgressBar
    override fun onStart() {
        super.onStart()
        //presenter.firstlyLoadNews()
        Log.v("time", Calendar.getInstance().timeInMillis.toString())
        val api = BotReportApi.retrofitService.getLiveEvents()
        launch(Dispatchers.Main) {
            // Try catch block to handle exceptions when calling the API.
            try {
                api.enqueue(object : Callback<LiveNews> {
                    override fun onFailure(call: Call<LiveNews>, t: Throwable) {
                        Log.e("network", call.request().url().toString())
                        Log.e("network", t.toString())

                    }

                    override fun onResponse(call: Call<LiveNews>, response: Response<LiveNews>) {
                        Log.e("network", response.body().toString())
                        if (response.body() != null)
                            setInAdapter(response.body()!!.liveNews as ArrayList<LiveEvent>)

                    }
                })
            }
            catch (e:Exception){
            }
            finally {
                Log.v("time", Calendar.getInstance().timeInMillis.toString())
            }



        }

    }

    private lateinit var adapter: LiveNewsAdapter
    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        _binding = LiveNewsFeedFragmentBinding.inflate(inflater, container, false)
        val view = binding.root
        recyclerView = binding.liveNewsRecycler
        recyclerAdapter = context?.let { LiveNewsAdapter(it, parentFragmentManager) }!!
        recyclerView.layoutManager = LinearLayoutManager(context)
        recyclerView.adapter = recyclerAdapter
        recyclerView.setItemViewCacheSize(3)
        shortAnimationDuration = resources.getInteger(android.R.integer.config_shortAnimTime)
        progressBar = binding.progressBar

            return view
        }

        override fun onDestroyView() {
            super.onDestroyView()
            _binding = null
        }

        override fun setInAdapter(result: ArrayList<LiveEvent>) {
            recyclerAdapter.setItems(result)
            crossfade()
            Log.v("time", Calendar.getInstance().timeInMillis.toString())
        }
    private fun crossfade() {
        recyclerView.apply {
            // Set the content view to 0% opacity but visible, so that it is visible
            // (but fully transparent) during the animation.
            alpha = 0f
            visibility = View.VISIBLE

            // Animate the content view to 100% opacity, and clear any animation
            // listener set on the view.
            animate()
                .alpha(1f)
                .setDuration(shortAnimationDuration.toLong())
                .setListener(null)
        }
        // Animate the loading view to 0% opacity. After the animation ends,
        // set its visibility to GONE as an optimization step (it won't
        // participate in layout passes, etc.)
        progressBar.animate()
            .alpha(0f)
            .setDuration(shortAnimationDuration.toLong())
            .setListener(object : AnimatorListenerAdapter() {
                override fun onAnimationEnd(animation: Animator) {
                    progressBar.visibility = View.GONE
                }
            })

    }
    }


