<template>
  <section>
    <div class="container p-5">
      <div class="row mb-5 text-center text-white">
        <div class="col-lg-10 mx-auto">
          <h1 class="display-4">SDG Label Classifier</h1>
          <p class="lead">
            Classify the contents of a PDF to their relavant Sustainable Goal
            Developlent Labels as prescribed by the United Nations
          </p>
        </div>
      </div>
      <!-- End -->

      <div class="row">
        <div class="col-lg-5 mx-auto">
          <div class="p-5 bg-white shadow rounded-lg">
            <h6 class="text-center mb-4 text-muted">Use text</h6>
            
            <div class="row">
              <div class="col">
                <textarea class="form-control" v-model="text" placeholder="Type in or paste any text segment of at least 20 words"></textarea>
              </div>

            </div>

            <div class="row mt-5 mb-4">
              <div class="col">
                <button
                  class="btn-primary btn-block rounded-pill shadow"
                  @click="classifyText"
                >
                  Label
                </button>
              </div>
            </div>

            <h6 class="text-center mb-4 text-muted">Use PDF</h6>

            <div class="row">
              <div class="col">
                <label
                  for="fileUpload"
                  class="
                    file-upload
                    btn btn-primary btn-block
                    rounded-pill
                    shadow
                  "
                  ><i class="fa fa-upload mr-2"></i>{{ upload_ph }}
                  <input ref="file" accept="application/pdf" id="fileUpload" type="file" @change="selectFile"/>
                </label>
              </div>
            </div>

            <div class="row mt-3">
              <div class="col-6">
                <input type="text" class="form-control" v-model="start" placeholder="Start Pg.No" />
              </div>

              <div class="col-6">
                <input type="text" class="form-control" v-model="end" placeholder="End Pg.No" />
              </div>
            </div>

            <div class="row mt-5">
              <div class="col">
                <button
                  class="btn-primary btn-block rounded-pill shadow"
                  @click="classifyPDF"
                >
                  Label
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from 'axios';

export default {
  name: "App",
  data() {
    return {
      text: '',
      start: '',
      end: '',
      file: '',
      upload_ph: 'Browse for file ...'
    };
  },

  methods: {
    async classifyText() {
      const response = await axios.post('http://vigneshwarans.pythonanywhere.com/classify', {text: this.text});

      console.log(this.convertToNormal(response.data));
    },

    selectFile(){
      this.file = this.$refs.file.files[0];
      this.upload_ph = this.file.name;
    },

    async classifyPDF() {
      var payload = new FormData();
      payload.append('start', this.start);
      payload.append('end', this.end);
      payload.append('file', this.file);

      const response = await axios.post('http://vigneshwarans.pythonanywhere.com/classifyPDF', payload);
      console.log(this.convertToNormal(response.data));

      this.start = this.end = this.file = '';
      this.upload_ph = 'Browse for file ...';
    },

    convertToNormal(obj) {
      return JSON.parse(JSON.stringify(obj));
    }
  },
};
</script>

<style>
.file-upload input[type="file"] {
  display: none;
}

body {
  background: #00b4db;
  background: -webkit-linear-gradient(to right, #0083b0, #00b4db);
  background: linear-gradient(to right, #0083b0, #00b4db);
  height: 100vh;
}

.rounded-lg {
  border-radius: 1rem;
}

.custom-file-label.rounded-pill {
  border-radius: 50rem;
}

.custom-file-label.rounded-pill::after {
  border-radius: 0 50rem 50rem 0;
}
</style>
