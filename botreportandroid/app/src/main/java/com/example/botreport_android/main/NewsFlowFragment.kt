package com.example.botreport_android.main

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageButton
import androidx.fragment.app.Fragment
import androidx.viewpager2.adapter.FragmentStateAdapter
import androidx.viewpager2.widget.ViewPager2
import com.arellomobile.mvp.MvpAppCompatFragment
import com.example.botreport_android.R
import com.example.botreport_android.presenter.NewsFlowPresenter
import com.example.botreport_android.ui.ArticleFeedFragment
import com.example.botreport_android.ui.LiveNewsFeedFragment
import com.example.botreport_android.views.NewsFlowView
import com.google.android.material.tabs.TabLayout
import com.google.android.material.tabs.TabLayoutMediator
import dagger.hilt.android.AndroidEntryPoint
import kotlinx.coroutines.flow.onEach
import moxy.presenter.InjectPresenter
import moxy.presenter.ProvidePresenter
import reactivecircus.flowbinding.android.view.clicks
import javax.inject.Inject
import javax.inject.Provider


@AndroidEntryPoint
class NewsFragment : MvpAppCompatFragment(), NewsFlowView {
    @InjectPresenter
    internal lateinit var flowPresenter: NewsFlowPresenter

    @Inject
    lateinit var flowPresenterProvider: Provider<NewsFlowPresenter>

    @ProvidePresenter
    fun providePresenter(): NewsFlowPresenter? {
        return flowPresenterProvider.get()
    }

    private lateinit var viewAdapter: ViewAdapter
    private lateinit var viewPager: ViewPager2
    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        val view: View = inflater.inflate(
            R.layout.news__flow_fragment,
            container, false
        )
        val buttonToSetting = view.findViewById<ImageButton>(R.id.button_to_settings)
        buttonToSetting.clicks().onEach {

        }
        return view
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        viewAdapter = ViewAdapter(this)
        viewPager = view.findViewById(R.id.pager)
        viewPager.adapter = viewAdapter
        val tabLayout: TabLayout = view.findViewById(R.id.menu)
        TabLayoutMediator(tabLayout, viewPager) { tab, position ->
            if(position==0){
                tab.text = resources.getString(R.string.live_news)
            }
            else{
                tab.text = resources.getString(R.string.articles)
            }
            viewPager.setCurrentItem(tab.position, true)
        }.attach()
    }

}

class ViewAdapter(fragment: Fragment) : FragmentStateAdapter(fragment) {

    override fun getItemCount(): Int = 2

    override fun createFragment(position: Int): Fragment {
        // Return a NEW fragment instance in createFragment(int)
        if(position==0) {
           return LiveNewsFeedFragment()
        }
        else{
           return ArticleFeedFragment()
        }
    }
}
