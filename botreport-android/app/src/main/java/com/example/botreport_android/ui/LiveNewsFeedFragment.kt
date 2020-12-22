package com.example.botreport_android.ui

import android.content.Context
import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.fragment.app.FragmentManager
import androidx.fragment.app.add
import androidx.fragment.app.commit
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.example.botreport_android.R
import com.example.botreport_android.adapters.LiveNewsAdapter
import com.example.botreport_android.databinding.ItemLiveNewsBinding
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
import javax.inject.Inject
import javax.inject.Provider

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
    override fun onStart() {
        super.onStart()
        presenter.firstlyLoadNews()

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
        val api = BotReportApi.retrofitService.getLiveEvents()
        launch(Dispatchers.Main) {
            // Try catch block to handle exceptions when calling the API.
            binding.progressBar.visibility = View.VISIBLE
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
            binding.progressBar.visibility = View.VISIBLE

        }
            return view
        }

        override fun onDestroyView() {
            super.onDestroyView()
            _binding = null
        }

        override fun setInAdapter(result: ArrayList<LiveEvent>) {
            recyclerAdapter.setItems(result)
        }


    }

