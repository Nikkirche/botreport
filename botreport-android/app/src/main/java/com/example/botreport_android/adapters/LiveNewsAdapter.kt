package com.example.botreport_android.adapters

import android.content.Context
import android.util.Log
import android.view.LayoutInflater
import android.view.ViewGroup
import android.widget.TextView
import androidx.fragment.app.FragmentManager
import androidx.fragment.app.add
import androidx.fragment.app.commit
import androidx.recyclerview.widget.RecyclerView
import com.example.botreport_android.R
import com.example.botreport_android.databinding.ItemLiveNewsBinding
import com.example.botreport_android.entities.LiveEvent
import com.example.botreport_android.ui.LiveEventDetailInfo
import com.example.botreport_android.ui.LiveNewsFeedFragment
import kotlinx.coroutines.flow.launchIn
import kotlinx.coroutines.flow.onEach
import reactivecircus.flowbinding.android.view.clicks

class LiveNewsAdapter(var context: Context,val fragmentManager: FragmentManager) :
    RecyclerView.Adapter<LiveNewsAdapter.LiveNewsViewHolder>() {
    lateinit var binding: ItemLiveNewsBinding
    var list:ArrayList<LiveEvent> = arrayListOf()
    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): LiveNewsViewHolder {
        binding = ItemLiveNewsBinding.inflate(LayoutInflater.from(parent.context), parent, false)

        return LiveNewsViewHolder(binding)
    }

    override fun onBindViewHolder(holder: LiveNewsViewHolder, position: Int) {
        holder.itemView.setOnClickListener {
            fragmentManager.commit {
                add(R.id.main_news,LiveEventDetailInfo())
            }
        }
        holder.bind(list[position])

    }

    fun setItems(list: ArrayList<LiveEvent>) {
        this.list = list
        Log.e("why",list.toString())
        notifyDataSetChanged()

    }

    override fun getItemCount(): Int = list.size
    inner class LiveNewsViewHolder(
        binding: ItemLiveNewsBinding
    ) :
        RecyclerView.ViewHolder(binding.getRoot()) {
        private lateinit var TextView: TextView
        private lateinit var DataView: TextView
        //private var LeagueView: Button
        //private var PlayerView: Button

        fun bind(liveEvent: LiveEvent) {
            DataView = binding.dataView
            TextView = binding.textView
            DataView.text = liveEvent.data
            TextView.text = liveEvent.text
            //LeagueView = binding.leaguaView
            //PlayerView = binding.playerView
        }

    }

}