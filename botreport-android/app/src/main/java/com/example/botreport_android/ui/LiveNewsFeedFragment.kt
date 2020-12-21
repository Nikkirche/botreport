package com.example.botreport_android.ui

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.TextView
import androidx.fragment.app.FragmentManager
import androidx.fragment.app.add
import androidx.fragment.app.commit
import androidx.lifecycle.Lifecycle
import androidx.lifecycle.LifecycleCoroutineScope
import androidx.lifecycle.lifecycleScope
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.example.botreport_android.R
import com.example.botreport_android.databinding.ItemLiveNewsBinding
import com.example.botreport_android.databinding.LiveNewsFeedFragmentBinding
import com.example.botreport_android.entities.LiveNews
import com.example.botreport_android.main.MainActivity
import com.example.botreport_android.main.NewsFlowFragment
import dagger.hilt.android.AndroidEntryPoint
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.flow.launchIn
import kotlinx.coroutines.flow.onEach
import moxy.MvpAppCompatFragment
import reactivecircus.flowbinding.android.view.clicks

@AndroidEntryPoint
class LiveNewsFeedFragment : MvpAppCompatFragment() {
    private val listLiveEvents = listOf(
        LiveNews(
            "GOOOOOAL!!! FURLONG DARNELL!1:2! Where’s the defense of Newcastle United gone?",
            "19/02/2020 /20:00",
            "Champions league",
            "FURLONG DARNELL"
        ),
        LiveNews(
            "IVANOVIC BRANISLAV skhlopotal gorchichnik JFYUFJFUUFUFGUUJDYJ ",
            "19/02/2020 20:04",
            "Champions league", "IVANOVIC BRANISLAV"
        ),
    )
    private var _binding: LiveNewsFeedFragmentBinding? = null
    private val binding get() = _binding!!

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        _binding = LiveNewsFeedFragmentBinding.inflate(inflater, container, false)
        val view = binding.root
        val layoutManager: RecyclerView.LayoutManager = LinearLayoutManager(context)
        binding.liveNewsRecycler.layoutManager = layoutManager
        val adapter = LiveNewsAdapter(listLiveEvents,parentFragmentManager)
        binding.liveNewsRecycler.adapter = adapter
        return view
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }

}

class LiveNewsAdapter(private val list: List<LiveNews>, val fragmentManager: FragmentManager) :
    RecyclerView.Adapter<LiveNewsAdapter.LiveNewsViewHolder>() {
    lateinit var binding: ItemLiveNewsBinding
    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): LiveNewsViewHolder {
        binding = ItemLiveNewsBinding.inflate(LayoutInflater.from(parent.context), parent, false)

        return LiveNewsViewHolder(binding,fragmentManager)
    }

    override fun onBindViewHolder(holder: LiveNewsViewHolder, position: Int) {
        val liveNews: LiveNews = list[position]
        holder.bind(liveNews)
        holder.itemView.setOnClickListener {

            fragmentManager.commit {
                setReorderingAllowed(true)
                add<LiveEventDetailInfo>(R.id.main_news)
                addToBackStack("detail_info")

            }
        }
    }

    override fun getItemCount(): Int = list.size
    inner class LiveNewsViewHolder(val binding: ItemLiveNewsBinding,val fragmentManager: FragmentManager) :
        RecyclerView.ViewHolder(binding.getRoot()) {
        private var TextView: TextView
        private var DataView: TextView
        private var LeagueView: Button
        private var PlayerView: Button

        init {
            DataView = binding.dataView
            TextView = binding.textView
            LeagueView = binding.leaguaView
            PlayerView = binding.playerView
        }

        fun bind(news: LiveNews) {
            DataView.text = news.data
            TextView.text = news.text
            LeagueView.text = news.league
            PlayerView.text = news.player
            LeagueView.setOnClickListener { GoToTagsFragment(news.league,fragmentManager) }
            PlayerView.setOnClickListener { GoToTagsFragment(news.player,fragmentManager) }
        }
        fun GoToTagsFragment(name:String,fragmentManager: FragmentManager){
            fragmentManager.commit {
                setReorderingAllowed(true)
                add<TagFragment>(R.id.main_news)
                addToBackStack(name)
            }
        }

    }
}