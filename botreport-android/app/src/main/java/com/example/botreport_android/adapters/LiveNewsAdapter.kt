package com.example.botreport_android.adapters

import android.content.Context
import android.view.LayoutInflater
import android.view.ViewGroup
import android.widget.Button
import android.widget.FrameLayout
import android.widget.ImageView
import android.widget.TextView
import androidx.appcompat.content.res.AppCompatResources.getDrawable
import androidx.fragment.app.FragmentManager
import androidx.fragment.app.commit
import androidx.recyclerview.widget.RecyclerView
import com.example.botreport_android.R
import com.example.botreport_android.databinding.ItemLiveNewsFlowBinding
import com.example.botreport_android.entities.LiveEvent
import com.wajahatkarim3.easyflipview.EasyFlipView

class LiveNewsAdapter(var context: Context,val fragmentManager: FragmentManager) :
    RecyclerView.Adapter<LiveNewsAdapter.LiveNewsViewHolder>() {
    lateinit var binding: ItemLiveNewsFlowBinding
    var list:ArrayList<LiveEvent> = arrayListOf()
    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): LiveNewsViewHolder {

        binding = ItemLiveNewsFlowBinding.inflate(LayoutInflater.from(parent.context), parent, false)

        return LiveNewsViewHolder(binding)
    }

    override fun onBindViewHolder(holder: LiveNewsViewHolder, position: Int) {
        /*holder.itemView.setOnClickListener {
            fragmentManager.commit {
                add(R.id.main_news,LiveEventDetailInfo())
            }
        }*/
        holder.bind(list[position])

    }

    fun setItems(list: ArrayList<LiveEvent>) {
        this.list = list
        notifyDataSetChanged()

    }

    override fun getItemCount(): Int = list.size
    inner class LiveNewsViewHolder(
        binding: ItemLiveNewsFlowBinding
    ) :
        RecyclerView.ViewHolder(binding.getRoot()) {
        private val backSide: FrameLayout = binding.backSide.root
        private val frontSide: FrameLayout = binding.frontSide.root
        private val flipView: EasyFlipView = binding.flipView
        lateinit var dataView:TextView
        lateinit var textView:TextView
        lateinit var playerView: Button
        lateinit var typeEventView:ImageView
        lateinit var generatedTextView: TextView
        lateinit var matchView: TextView
        lateinit var  leaguaView:TextView

        //private var LeagueView: Button
        //private var PlayerView: Button
        init {
            backSide.setOnClickListener {
                flipView.flipDuration = 1000
                flipView.flipTheView()
            }
            frontSide.setOnClickListener {
                flipView.flipDuration = 1000
                flipView.flipTheView()
            }
        }

        fun bind(liveEvent: LiveEvent) {
            dataView= binding.frontSide.dataView
            textView = binding.frontSide.textView
            playerView = binding.frontSide.playerView
            generatedTextView = binding.backSide.generatedTextView
            leaguaView = binding.frontSide.leaguaView
            matchView = binding.frontSide.matchView
            typeEventView = binding.frontSide.typeEventView
            dataView.text = liveEvent.data
            textView.text = liveEvent.text
            playerView.text = liveEvent.player
            generatedTextView.text = liveEvent.generatedText
            matchView.text = liveEvent.match
            leaguaView.text = liveEvent.leagua
            when(liveEvent.type){
                ("YELLOW_CARD"),("YELLOW_RED_CARD")-> typeEventView.setImageDrawable(getDrawable (context,R.drawable.ic_yellow_card))
                ("RED_CARD")-> typeEventView.setImageDrawable(getDrawable(context,R.drawable.ic_red_card))
                else -> typeEventView.setImageDrawable(getDrawable(context,R.drawable.ic_goal))
            }





        }

    }

}