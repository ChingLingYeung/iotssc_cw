package com.example.iotsscapp;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;
import okhttp3.OkHttpClient;
import okhttp3.logging.HttpLoggingInterceptor;
import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

import android.os.Bundle;
import android.os.Handler;
import android.util.Log;
import android.widget.TextView;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.TimeUnit;

public class MainActivity extends AppCompatActivity {

    RecyclerView recyclerView;
    ArrayList<String> ts = new ArrayList<>();
    ArrayList<String> cls = new ArrayList<>();

    private int mInterval = 5000;
    private Handler mHandler;
    boolean shouldStopLoop = false;

    Runnable runnable = new Runnable() {
        @Override
        public void run() {
            Log.d("Get","in run, polling");
            getDatabaseResponse();
            if (!shouldStopLoop) {
                mHandler.postDelayed(this, 5000);
            }
        }
    };

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        recyclerView = findViewById(R.id.recyclerView);

        MyAdapter myAdapter = new MyAdapter(this,ts,cls);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));
        recyclerView.setAdapter(myAdapter);

        mHandler = new Handler();
        startRepeatingTask();

        getDatabaseResponse();
    }

    @Override
    public void onDestroy() {
        super.onDestroy();
        stopRepeatingTask();
    }

    Runnable mStatusChecker = new Runnable() {
        @Override
        public void run() {
            try {
                getDatabaseResponse(); //this function can change value of mInterval.
            } finally {
                // 100% guarantee that this always happens, even if
                // your update method throws an exception
                mHandler.postDelayed(mStatusChecker, mInterval);
            }
        }
    };

    void startRepeatingTask() {
        mStatusChecker.run();
    }

    void stopRepeatingTask() {
        mHandler.removeCallbacks(mStatusChecker);
    }

    private void getDatabaseResponse() {
//        DatabaseAPI databaseAPI = APIClient.getClient().create(DatabaseAPI.class);
        HttpLoggingInterceptor logging = new HttpLoggingInterceptor();
        // set your desired log level
        logging.setLevel(HttpLoggingInterceptor.Level.BODY);

        final OkHttpClient okHttpClient = new OkHttpClient.Builder()
                .readTimeout(30, TimeUnit.SECONDS)
                .connectTimeout(30, TimeUnit.SECONDS)
                .addInterceptor(logging)
                .build();

        final Retrofit retrofit = new Retrofit.Builder()
                .baseUrl("http://35.197.198.128:2333/")
                .addConverterFactory(GsonConverterFactory.create())
                .build();

        DatabaseAPI databaseAPI = retrofit.create(DatabaseAPI.class);
        Call<List<Sample>> call = databaseAPI.getSamples();

        call.enqueue(new Callback<List<Sample>>() {
            @Override
            public void onResponse(Call<List<Sample>> call, Response<List<Sample>> response) {
                Log.d("Get", "on response");
                if (response.isSuccessful()) {
                    List<Sample> sampleList = response.body();
                    Sample latestSample = sampleList.get(sampleList.size() - 1);
                    Log.d("Get", String.valueOf(sampleList.size()) + " Samples retrieved");
                    int count = 0;
                    for (Sample sample : sampleList){
                        count += 1;
                        String sample_ts = sample.getTimestamp();
                        int sample_cls = sample.getClassification();
                        ts.add(0, sample_ts);
                        if(sample_cls == 0){
                            cls.add(0, "Walk");
                        }
                        else{
                            cls.add(0, "Run");
                        }

                    }
                    Log.d("Get", String.valueOf(count) + " Samples processed");
                    int classification = latestSample.getClassification();

                    TextView textView = findViewById(R.id.classification);
                    if (classification == 0){
                        textView.setText("You are Walking");
                    }
                    else{
                        textView.setText("You are Running");
                    }
                } else {
                    Log.d("Get", "response not successful!");
                    return;
                }
            }

            @Override
            public void onFailure(Call<List<Sample>> call, Throwable t) {
                Log.d("Get", "on failure");
            }

        });

    }
}
